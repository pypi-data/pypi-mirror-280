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

# Main function
def main():
    parser = argparse.ArgumentParser(description='Fetch and save Power BI tables.')
    parser.add_argument('--server', required=True, help='Power BI server URL')
    parser.add_argument('--db_name', required=True, help='Database name')
    parser.add_argument('--username', required=True, help='Username')
    parser.add_argument('--password', required=True, help='Password')
    parser.add_argument('--tables', required=True, nargs='+', help='List of tables to download')
    args = parser.parse_args()

    conn_str = set_conn_string(args.server, args.db_name, args.username, args.password)
    for table in args.tables:
        fetch_and_save_table(table, conn_str, f"{table}.parquet")

if __name__ == '__main__':
    main()
