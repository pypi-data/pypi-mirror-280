import pandas as pd

from monzy.utils import sql_templates
from monzy.utils.custom_logger import logger

compare_transaction_cols = [
    "id",
    "timestamp",
    "description",
    "amount",
    "category",
    "notes",
]


def _get_db_transactions(db: object, table: str) -> pd.DataFrame:
    """Fetch transactions from the database.

    Args:
        db (object): Database connection object.
        table (str): Name of the table to fetch transactions from.

    Returns:
        pd.DataFrame: DataFrame containing the transactions fetched from the database.
    """
    db_transactions = db.query(
        sql=sql_templates.exists.format(table=table),
        return_data=True,
    )

    return db_transactions


def get_new_transactions(db: object, table: str, fetched_transactions: pd.DataFrame):
    """Identify new transactions that are not present in the database.

    Args:
        db (object): Database connection object.
        table (str): Name of the table to check transactions against.
        fetched_transactions (pd.DataFrame): DataFrame containing fetched transactions.

    Returns:
        pd.DataFrame: DataFrame containing new transactions to be uploaded.
    """
    db_transactions = _get_db_transactions(db, table)

    db_ids_lst = db_transactions["id"].tolist()

    new_transaction_ids = []
    for item in fetched_transactions["id"].tolist():
        if item not in db_ids_lst:
            new_transaction_ids.append(item)

    transactions_to_upload = fetched_transactions[
        fetched_transactions["id"].isin(new_transaction_ids)
    ].reset_index(drop=True)

    return transactions_to_upload


def get_changed_transaction_ids(
    db: object, table: str, fetched_transactions: pd.DataFrame
) -> pd.DataFrame:
    """Identify transactions that have changed based on a set of columns.

    Args:
        db (object): Database connection object.
        table (str): Name of the table to check transactions against.
        fetched_transactions (pd.DataFrame): DataFrame containing fetched transactions.

    Returns:
        pd.DataFrame: DataFrame containing IDs of changed transactions.
    """
    db_transactions = _get_db_transactions(db, table)
    db_transactions["date"] = pd.to_datetime(db_transactions["date"])
    db_transactions["amount"] = db_transactions["amount"].round(2)
    db_transactions_cols_to_compare = db_transactions[compare_transaction_cols]

    fetched_transactions_cols_to_compare = fetched_transactions[compare_transaction_cols]
    ufetched_transactions_ids = fetched_transactions["id"].tolist()

    # Get transactions from db filtered by ids from transactions upstream
    filtered_db_transactions = db_transactions_cols_to_compare[
        db_transactions_cols_to_compare["id"].isin(ufetched_transactions_ids)
    ]
    filtered_db_transactions_cols_to_compare = filtered_db_transactions.reset_index(
        drop=True
    ).sort_values("timestamp")
    fetched_transactions_cols_to_compare = fetched_transactions_cols_to_compare.reset_index(
        drop=True
    ).sort_values("timestamp")

    # Step 1: Merge the DataFrames on 'id'
    merged_transactions = pd.merge(
        fetched_transactions_cols_to_compare,
        filtered_db_transactions_cols_to_compare,
        on="id",
        suffixes=("_fetched", "_db"),
    )

    # Initialize a DataFrame for differences
    differences = pd.DataFrame()

    for col in compare_transaction_cols:
        if col != "id":
            # For each column, check if the values in the merged DataFrame are different
            differences[col] = merged_transactions[f"{col}_fetched"].ne(
                merged_transactions[f"{col}_db"]
            )

    # Step 3: Filter rows with any differences
    # Use 'any(axis=1)' to check each row - if any column is different, the row will be included
    merged_transactions = merged_transactions[differences.any(axis=1)]
    changed_transactions_ids_since_20240105 = merged_transactions[
        merged_transactions["timestamp_db"] > pd.to_datetime("2024-01-05")
    ]["id"].to_list()
    return changed_transactions_ids_since_20240105


def upload_new_transactions(db: object, table: str, transactions_to_upload: pd.DataFrame) -> None:
    """Upload new transactions to the database.

    Args:
        db (object): Database connection object.
        table (str): Name of the table to insert transactions into.
        transactions_to_upload (pd.DataFrame): DataFrame containing transactions to be uploaded.

    Returns:
        None
    """
    db.insert(db, table, transactions_to_upload)
    logger.info("Uploaded new transactions")


def update_changed_transactions(db: object, table: str, changed_transactions: pd.DataFrame) -> None:
    """Update changed transactions in the database.

    Args:
        db (object): Database connection object.
        table (str): Name of the table to update transactions in.
        changed_transactions (pd.DataFrame): DataFrame containing changed transactions.

    Returns:
        None
    """
    transactions_to_delete_ids_str = str(changed_transactions["id"].to_list()).strip("[").strip("]")

    db.delete(db, table, transactions_to_delete_ids_str)

    db.insert(db, table, changed_transactions)
    num_changed_transactions = len(changed_transactions)
    logger.info(f"Updated {num_changed_transactions} changed transactions")
