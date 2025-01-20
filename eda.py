import matplotlib.pyplot as plt
import seaborn as sns

# Plot stock trends
def plot_stock_trend(df, symbol):
    stock_data = df[df['symbol'] == symbol]
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['business_date'], stock_data['close_price'], label=f"{symbol} Close Price")
    plt.title(f"{symbol} Stock Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.legend()
    plt.show()

# Plot distribution of returns
def plot_return_distribution(df):
    df['return'] = df['close_price'].pct_change()
    plt.figure(figsize=(10, 6))
    sns.histplot(df['return'].dropna(), bins=50, kde=True)
    plt.title("Distribution of Daily Returns")
    plt.xlabel("Return")
    plt.ylabel("Frequency")
    plt.show()

# Correlation matrix
def plot_correlation_matrix(df):
    correlation_matrix = df[['close_price', 'total_traded_quantity', 'total_traded_value']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()

# Example usage
