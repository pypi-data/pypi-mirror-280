import argparse
import polars as pl
from download_xmla.ssas_api import set_conn_string, get_DAX

# Function to fetch and save table data
def fetch_and_save_table(table_name, conn_str, file_name):
    query = f'EVALUATE {table_name}'
    try:
        df = get_DAX(conn_str, query)
        pl_df = pl.DataFrame(df)
        print(f"Table '{table_name}' fetched successfully!")
        pl_df.write_parquet(file_name)
        print(f"Table '{table_name}' saved to {file_name}")
    except Exception as e:
        print(f"Failed to fetch or save table '{table_name}'.")
        print(str(e))

# Main function to be called from external script
def fetch_tables(server, db_name, username, password, tables):
    conn_str = set_conn_string(server, db_name, username, password)
    for table in tables:
        fetch_and_save_table(table, conn_str, f"{table}.parquet")

# Optional: main function for command-line usage (if needed)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch and save Power BI tables.')
    parser.add_argument('--server', required=True, help='Power BI server URL')
    parser.add_argument('--db_name', required=True, help='Database name')
    parser.add_argument('--username', required=True, help='Username')
    parser.add_argument('--password', required=True, help='Password')
    parser.add_argument('--tables', required=True, nargs='+', help='List of tables to download')
    args = parser.parse_args()

    fetch_tables(
        server=args.server,
        db_name=args.db_name,
        username=args.username,
        password=args.password,
        tables=args.tables
    )
