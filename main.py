import pandas as pd

from pre_processing import main as processing_main
from eda import plot_stock_trend, plot_return_distribution, plot_correlation_matrix


def main(combined_data: pd.DataFrame = processing_main()):
    plot_stock_trend(combined_data, symbol="NABIL")
    plot_return_distribution(combined_data)
    plot_correlation_matrix(combined_data)


if __name__ == "__main__":
    main()