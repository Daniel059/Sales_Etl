# importing the required module
import pandas as pd
import os

def run_etl(input_file_path,output_dir):
    # 1.Extract
    print(f"Loading Data from {input_file_path}...")
    df = pd.read_csv(input_file_path)
    print("Data Loaded Successfully.")
    
    # 2.Transform
    print("Transforming Data...")
    # Converting order_date to datetime format
    df['order_date'] = pd.to_datetime(df['order_date'])
    
    # Calculating total_price
    df['total_price'] = df['quantity'] * df['price_per_unit']
    
    # Converting relevant IDs to string/object if they are not meant for calculations
    df['order_id'] = df['order_id'].astype(str)
    df['customer_id'] = df['customer_id'].astype(str)
    df['product_id'] = df['product_id'].astype(str)
    print("Data Transformation Complete.")
    
    # 3.Load
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir,'processed_sales_data.csv')
    df.to_csv(output_file_path,index=False)
    print(f"Processed Data Saved to {output_file_path}.")

if __name__ == "__main__":
        input_csv = 'data/dataset.csv'
        output_directory = 'processed_data'
        run_etl(input_csv, output_directory)