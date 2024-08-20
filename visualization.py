import pandas as pd
from utils import data_dir, return_files

from _parser import _parser as pre_processing

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_line_chart(df):
    # 1. Line plot of close price over time
    plt.figure(figsize=(10, 6))
    plt.plot(df['business_date'], df['close_price'], label='Close Price')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title('Stock Close Price Over Time')
    plt.legend()
    plt.show()


def main(path: str):
    files = return_files(path)

    for file in files:
        df = pd.read_csv(file)
        df = pre_processing(df)

        if len(df) == 0:
            continue

        plot_line_chart(df)
        exit()


if __name__ == "__main__":
    main(data_dir)
