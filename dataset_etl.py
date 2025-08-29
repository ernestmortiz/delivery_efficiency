import pandas as pd
import numpy as np

try:
    # Load data from the CSV file.
    df = pd.read_csv('dataset.csv')
    print("Original dataset shape:", df.shape)

    # --- Data Cleaning ---

    # 1. Change time columns to datetime format.
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
    df['actual_delivery_time'] = pd.to_datetime(df['actual_delivery_time'], errors='coerce')

    # 2. Set negative numbers in key columns to 0.
    numeric_cols_to_clean = ['min_item_price', 'total_onshift_partners', 'total_busy_partners', 'total_outstanding_orders']
    for col in numeric_cols_to_clean:
        df.loc[df[col] < 0, col] = 0
    print("Negative values in key columns cleaned.")

    # 3. Fill in missing (blank) values.
    # Fill missing numbers with the median value for that column.
    for col in ['total_onshift_partners', 'total_busy_partners', 'total_outstanding_orders']:
        median_val = df[col].median()
        df[col].fillna(median_val, inplace=True)
    
    # Fill missing text with 'Unknown'.
    df['store_primary_category'].fillna('Unknown', inplace=True)
    # Fill with the most frequent market ID.
    df['market_id'].fillna(df['market_id'].mode()[0], inplace=True)
    print("Missing values handled.")

    # --- Create New Columns ---

    # 1. Create 'delivery_duration_minutes' column.
    df['delivery_duration_minutes'] = (df['actual_delivery_time'] - df['created_at']).dt.total_seconds() / 60

    # 2. Create 'partner_utilization_rate' column.
    df['partner_utilization_rate'] = df['total_busy_partners'] / df['total_onshift_partners']
    # Fix any division-by-zero errors.
    df['partner_utilization_rate'].replace([np.inf, -np.inf], 0, inplace=True)
    df['partner_utilization_rate'].fillna(0, inplace=True)
    print("New features 'delivery_duration_minutes' and 'partner_utilization_rate' created.")

    # Remove any rows where delivery duration could not be calculated.
    df.dropna(subset=['delivery_duration_minutes'], inplace=True)

    # --- Save the Final Data ---
    
    # Save the cleaned data to a new CSV file.
    output_filename = 'cleaned_delivery_data.csv'
    df.to_csv(output_filename, index=False)
    print(f"\nSuccessfully cleaned data and saved to '{output_filename}'")
    
    # Show a preview of the new, cleaned data.
    print("\nFirst 5 rows of the new, cleaned dataset:")
    print(df[['created_at', 'delivery_duration_minutes', 'partner_utilization_rate', 'store_primary_category']].head())
    
    # Show the summary of the new, cleaned data.
    print("\nNew dataset info:")
    df.info()

except FileNotFoundError:
    print("Error: 'dataset.csv' not found. Please ensure the file is in the correct directory.")
except Exception as e:
    print(f"An error occurred: {e}")