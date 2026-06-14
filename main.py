import pandas as pd
from services.loading import read_csv
from services.cleaning import clean_data
from config import Config

for file in Config.RAW_DATA_DIR.glob("*.csv"):
    output_file= Config.CLEANED_DATA_DIR / file.name
    processed_files= Config.PROCESSED_DATA_DIR / file.name
    if  processed_files.exists():
        print(f"File {file.name} already processed. Skipping.")
        file.unlink()
        continue
    df= read_csv(file)
    cleaned_df= clean_data(df)
    cleaned_df.to_csv(output_file, index=False,decimal=',')
    df.to_csv(processed_files, index=False,decimal=',')
    file.unlink()
    print(f"Processed {file.name} and saved cleaned data to {output_file}.")
   

