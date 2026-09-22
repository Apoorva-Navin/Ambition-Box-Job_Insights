import pandas as pd
import os

base_dir = os.getcwd()   # AMBITION PROJECT
data_dir = os.path.join(base_dir, "scraped_data")

dataframes = []

for file in os.listdir(data_dir):
    if file.endswith("_processed.csv"):
        file_path = os.path.join(data_dir, file)
        print("Reading:", file_path)
        
        df = pd.read_csv(file_path)
        df["city"] = file.replace("_processed.csv", "")  # extract city name
        dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)

output_path = os.path.join(base_dir, "all_processed_combined.csv")
combined_df.to_csv(output_path, index=False)

print("✅ ALL CSV files combined successfully!")