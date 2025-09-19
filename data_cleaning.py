import pandas as pd
import numpy as np
import re

def clean_data(df):
    print("Cleaning data...")
    
    # Create a copy
    df_clean = df.copy()
    
    # Extract year from publish_time
    print("Extracting year...")
    years = []
    for date_str in df_clean['publish_time']:
        try:
            if pd.isna(date_str):
                years.append(np.nan)
                continue
                
            if isinstance(date_str, str):
                year_match = re.search(r'(\d{4})', date_str)
                if year_match:
                    years.append(int(year_match.group(1)))
                else:
                    years.append(np.nan)
            else:
                years.append(np.nan)
        except:
            years.append(np.nan)
    
    df_clean['publish_year'] = years
    
    # Remove rows without year
    initial_count = len(df_clean)
    df_clean = df_clean.dropna(subset=['publish_year'])
    print(f"Removed {initial_count - len(df_clean)} rows without year")
    
    # Fill missing values
    df_clean['journal'] = df_clean['journal'].fillna('Unknown')
    
    return df_clean

if __name__ == "__main__":
    df = pd.read_csv("metadata_sample.csv", low_memory=False)
    df_clean = clean_data(df)
    df_clean.to_csv("cleaned_metadata.csv", index=False)
    print(f"Cleaned data saved. Shape: {df_clean.shape}")