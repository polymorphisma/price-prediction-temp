import pandas as pd
import os
from utils import generate_file, return_files

stock_price_directory = r'/home/polymorphisma/self/StockAnalysis/data/stockwise'
save_directory = r'/home/polymorphisma/self/StockAnalysis/data/parsed'
float_columns = ['open_price', 'high_price', 'low_price', 'close_price', 'total_traded_quantity', 'total_traded_value']


def _segregate_csv(path: str):
    df = pd.read_csv(path)

    unique_symbol = set(df["SYMBOL"])

    for symbol in unique_symbol:
        temp_df = df[df['SYMBOL'] == symbol]
        temp_df.to_csv(generate_file(stock_price_directory, symbol), index=False)


def convert_to_float(row: float):
    return float(row)


def _parser(df):
    df.columns = [x.lower() for x in df.columns.to_list()]

    if len(df) < 100:
        return pd.DataFrame()

    for f_col in float_columns:
        df[f_col] = df[f_col].apply(convert_to_float)

    df['business_date'] = pd.to_datetime(df['business_date'])

    return df


def main(path: str, save_directory: str):
    files = return_files(path)
    for file in files:
        df = pd.read_csv(file)
        df = _parser(df)

        if len(df) == 0:
            continue

        symbol = df['symbol'][0]
        save_path = generate_file(save_directory, symbol)
        df.to_csv(save_path, index=False)


if __name__ == "__main__":
    main(stock_price_directory, save_directory)
