from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    RAW_DATA_DIR = os.getenv("RAW_DATA_DIR")
    PROCESSED_DATA_DIR = os.getenv("PROCESSED_DATA_DIR")
    CLEANED_DATA_DIR = os.getenv("CLEANED_DATA_DIR")