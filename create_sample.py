import pandas as pd
import random

def create_sample(input_file, output_file, sample_size=3000):
    print("Creating sample dataset...")
    
    try:
        # For large files, read in chunks
        chunk_list = []
        for chunk in pd.read_csv(input_file, chunksize=5000, low_memory=False):
            chunk_list.append(chunk)
            if len(chunk_list) >= 3:  # Limit to 3 chunks to save memory
                break
        
        # Combine all chunks
        full_df = pd.concat(chunk_list)
        print(f"Dataset loaded. Shape: {full_df.shape}")
        
        # Create sample
        if len(full_df) > sample_size:
            df_sample = full_df.sample(n=sample_size, random_state=42)
        else:
            df_sample = full_df
            
        print(f"Sample created with {len(df_sample)} rows")
        
        # Save the sample
        df_sample.to_csv(output_file, index=False)
        print(f"Sample saved to {output_file}")
        
        return df_sample
        
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    create_sample("metadata.csv", "metadata_sample.csv", 3000)