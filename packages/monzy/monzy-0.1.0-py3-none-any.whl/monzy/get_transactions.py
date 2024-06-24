from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from monzo.endpoints.transaction import Transaction

from monzy.utils.custom_logger import logger
from monzy.utils.date_utils import get_date_periods


def get_historic_transactions(
    monzo_auth: object, account_id: str, created_date: datetime
) -> pd.DataFrame:
    """Fetch historical transactions from Monzo API.

    Args:
        monzo_auth (object): Monzo authentication object.
        account_id (str): Monzo account ID.
        created_date (datetime): The starting date to fetch transactions from.

    Returns:
        pd.DataFrame: DataFrame containing fetched transactions.
    """
    fetched_transactions_lst = []
    periods = get_date_periods(created_date)
    logger.info(f"Using date range: {periods}")

    try:
        for since, before in periods:
            fetched_transactions = Transaction.fetch(
                auth=monzo_auth,
                account_id=account_id,
                since=since,
                before=before,
                expand=["merchant"],
            )
            fetched_transactions_lst.append(fetched_transactions)
            num_of_transactions = len(fetched_transactions)
            logger.info(
                f"Fetched {num_of_transactions} transactions for dates: {since} to {before}"
            )
    except Exception:
        logger.error(
            "Failed to fetch transactions for some dates - make sure to trigger DAG immediately after refreshing permissions"
        )

    fetched_transactions = [item for sublist in fetched_transactions_lst for item in sublist]

    return fetched_transactions


def get_transactions_list(monzo_auth: object, account_id: str) -> list:
    """Fetch recent transactions from Monzo API.

    Args:
        monzo_auth (object): Monzo authentication object.
        account_id (str): Monzo account ID.

    Returns:
        list: List of fetched transactions.
    """
    fetched_transactions_list = Transaction.fetch(
        auth=monzo_auth,
        account_id=account_id,
        since=datetime.today() - timedelta(days=30),
        expand=["merchant"],
    )
    logger.info(f"Fetched {len(fetched_transactions_list)} transactions")

    return fetched_transactions_list


def transform_transactions(fetched_transactions_list: list) -> pd.DataFrame:
    """Transform a list of fetched transactions into a DataFrame.

    Args:
        fetched_transactions_list (list): List of fetched transactions.

    Returns:
        pd.DataFrame: DataFrame containing transformed transactions.
    """
    transactions_data = []
    for trn in fetched_transactions_list:
        transactions_data.append(
            {
                "id": trn.transaction_id,
                "date": trn.created,
                "description": trn.description,
                "amount": trn.amount,
                "category": trn.category,
                "decline_reason": trn.decline_reason,
                "meta": trn.metadata,
                "merchant": trn.merchant,
                "currency": trn.currency,
                "local_currency": trn.local_currency,
                "local_amount": trn.local_amount,
            }
        )

    transactions_df = pd.DataFrame(transactions_data)

    transactions_df.rename(
        columns={
            "transaction_id": "id",
            "created": "date",
            "merchant": "merchant",
            "local_currency": "local_currency",
            "local_amount": "local_amount",
        },
        inplace=True,
    )

    return transactions_df


def normalise_transactions(transactions_df: pd.DataFrame) -> pd.DataFrame:
    """Normalise the transactions DataFrame by flattening JSON columns.

    Args:
        transactions_df (pd.DataFrame): DataFrame containing transactions.

    Returns:
        pd.DataFrame: Normalized DataFrame.
    """
    metadata = pd.json_normalize(transactions_df["meta"])
    transactions_df = transactions_df.merge(metadata, left_index=True, right_index=True)

    merchant_data = pd.json_normalize(transactions_df["merchant"])
    transactions_df = transactions_df.merge(merchant_data, left_index=True, right_index=True)

    columns_dict = {
        "id_x": "id",
        "id_y": "merchant_id",
        "name": "merchant_description",
        "category_x": "category",
        "category_y": "merchant_category",
    }
    transactions_df.rename(columns=columns_dict, inplace=True)

    return transactions_df


def process_transactions(
    transactions_df: pd.DataFrame, source: str, category_replacement_dct
) -> pd.DataFrame:
    """Process transactions DataFrame by formatting and adding necessary columns.

    Args:
        transactions_df (pd.DataFrame): DataFrame containing transactions.
        source (str): Source identifier to be added to the transactions.
        category_replacement_dct (dict): Dictionary for replacing category values.

    Returns:
        pd.DataFrame: Processed DataFrame.
    """
    # Replace categories and format them
    transactions_df["category"] = transactions_df["category"].replace(category_replacement_dct)
    transactions_df["category"] = transactions_df["category"].str.replace("_", " ").str.title()

    # Convert amount and local_amount to appropriate currency
    transactions_df["amount"] = -transactions_df["amount"] / 100
    transactions_df["local_amount"] = -transactions_df["local_amount"] / 100

    # Keep original currency where applicable
    transactions_df["currency"] = np.where(
        transactions_df["local_currency"] != "GBP",
        transactions_df["local_currency"].str.lower(),
        transactions_df["currency"].str.lower(),
    )

    # Drop unnecessary columns and reset index
    transactions_df.drop(columns=["local_currency"], inplace=True)
    transactions_df.reset_index(drop=True, inplace=True)

    # Add source column if provided
    if source:
        transactions_df["source"] = source

    # Create decline column based on decline_reason presence
    transactions_df["decline"] = np.where(transactions_df["decline_reason"].fillna("") == "", 0, 1)

    # Ensure all required columns are present and formatted correctly
    columns = [
        "id",
        "date",
        "description",
        "amount",
        "category",
        "merchant_description",
        "suggested_tags",
        "decline",
        "decline_reason",
        "currency",
        "source",
    ]
    for col in columns:
        if col not in transactions_df.columns:
            transactions_df[col] = None

    # Use merchant_description in place of description where available
    transactions_df["description"] = np.where(
        transactions_df["merchant_description"].notnull(),
        transactions_df["merchant_description"],
        transactions_df["description"],
    )

    # Rename suggested_tags to tags and drop merchant_description
    transactions_df.rename(columns={"suggested_tags": "tags"}, inplace=True)
    transactions_df.drop(columns=["merchant_description"], inplace=True)

    # Sort transactions by date
    transactions_df.sort_values("date", inplace=True)

    # Return only the specified columns
    return transactions_df[columns].copy()
