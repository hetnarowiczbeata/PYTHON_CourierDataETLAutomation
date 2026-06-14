import pandas as pd
from services.loading import read_csv
from services.cleaning import clean_data
from config import Config

for file in Config.RAW_DATA_DIR.glob("*.csv"):
    df= read_csv(file)
    cleaned_df= clean_data(df)
    output_file= Config.CLEANED_DATA_DIR / file.name
    cleaned_df.to_csv(output_file, index=False)
    processed_files= Config.PROCESSED_DATA_DIR / file.name
    df.to_csv(processed_files, index=False)


