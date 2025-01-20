import pandas as pd
import os
import glob

# Directories
save_directory = r'/home/polymorphisma/experiments/testing/data/parsed'
combined_csv_path = os.path.join(save_directory, "combined_stock_data.csv")

# Combine all stock CSV files into one dataset
def combine_stock_data(directory):
    all_files = glob.glob(os.path.join(directory, "*.csv"))
    df_list = [pd.read_csv(file) for file in all_files]
    combined_df = pd.concat(df_list, ignore_index=True)
    print(combined_df)
    combined_df['business_date'] = pd.to_datetime(combined_df['business_date'])
    return combined_df


def main():
    # Save the combined dataset
    combined_data = combine_stock_data(save_directory)
    combined_data.to_csv(combined_csv_path, index=False)
    print(f"Combined data saved to {combined_csv_path}")

    return combined_data
