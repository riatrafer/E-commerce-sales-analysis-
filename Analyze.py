import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# --- Data Generation ---
def generate_dummy_data(num_records=1000):
    """
    Generates a Pandas DataFrame with dummy e-commerce transaction data.
    """
    print("Generating dummy data...")
    # Create a date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    
    # Generate random dates
    dates = [start_date + timedelta(seconds=np.random.randint(0, int((end_date - start_date).total_seconds()))) for _ in range(num_records)]
    
    # Generate other columns
    products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam', 'Headphones']
    product_prices = {'Laptop': 1200, 'Mouse': 25, 'Keyboard': 75, 'Monitor': 300, 'Webcam': 50, 'Headphones': 100}
    
    data = {
        'OrderID': range(1, num_records + 1),
        'Date': dates,
        'Product': np.random.choice(products, num_records),
        'Quantity': np.random.randint(1, 5, num_records),
    }
    
    df = pd.DataFrame(data)
    
    # Add a 'Price' column based on the product
    df['Price'] = df['Product'].apply(lambda x: product_prices[x])
    
    # Calculate total sale
    df['TotalSale'] = df['Quantity'] * df['Price']
    
    print("Data generation complete.")
    return df

# --- Data Analysis ---
def analyze_data(df):
    """
    Performs basic analysis on the e-commerce data.
    """
    print("\n--- Data Analysis ---")
    
    # 1. Basic Information
    print("Data Head:")
    print(df.head())
    print("\nData Info:")
    df.info()
    print("\nDescriptive Statistics:")
    print(df.describe())
    
    # 2. Sales over time
    print("\nAnalyzing sales over time...")
    df_time = df.set_index('Date')
    monthly_sales = df_time['TotalSale'].resample('M').sum()
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=monthly_sales.index, y=monthly_sales.values)
    plt.title('Total Sales Over Time')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.savefig('sales_over_time.png')
    print("Saved 'sales_over_time.png'")
    
    # 3. Best-selling products
    print("\nAnalyzing best-selling products...")
    product_sales = df.groupby('Product')['TotalSale'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=product_sales.index, y=product_sales.values)
    plt.title('Total Sales by Product')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('sales_by_product.png')
    print("Saved 'sales_by_product.png'")
    
    print("\nAnalysis complete.")

# --- Main Execution ---
if __name__ == "__main__":
    # Generate and save data
    dummy_df = generate_dummy_data()
    dummy_df.to_csv('ecommerce_data.csv', index=False)
    print("Saved data to 'ecommerce_data.csv'")
    
    # Analyze the data
    analyze_data(dummy_df)

