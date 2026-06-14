# PYTHON_CourierDataETLPipeline


Automated ETL pipeline built with Python and Pandas for processing courier CSV datasets. It cleans raw files, saves ready-to-use outputs for BI reporting, and archives processed files to avoid duplicate processing. This reduces the need for Power Query transformations and improves report consistency.

**Project Structure**
raw_data/ Contains raw CSV files received from the data source
clean_data/ Stores cleaned and transformed CSV files
processed_data/ Archives source files that have already been processed. Once the ETL process is completed successfully, files are moved from raw_data to this directory to prevent duplicate processing

services/ 
Contains modules responsible for the application's business logic.
        loading.py/ Handles loading and reading source CSV files into Pandas DataFrames
        cleaning.py/ Contains data cleaning and transformation logic, such as removing unnecessary columns, standardizing data, and preparing datasets for further analysis

**During the data cleaning process, I noticed missing values in the VAS Charges column. Since Total Amount appears to be the sum of Tariff and VAS Charges, I calculated the missing VAS Charges values by subtracting Tariff from Total Amount. This calculation was applied only to records where VAS Charges was null, in order to avoid affecting valid data and to prevent issues in the future if missing values appear in either the Tariff or Total Amount columns.**

config.py/ Configuration file that stores paths to project directories: raw_data, clean_data,processed_data

main.py/ The main entry point of the application. Responsible for reading CSV files from the raw_data directory, executing the data cleaning and transformation process, saving processed files to the clean_data directory, archiving processed source files in the processed_data directory 

**To prevent duplicate processing, the pipeline checks whether a file with the same name already exists in the processed_data directory. If a matching file is found, the newly uploaded file is treated as a duplicate and removed from raw_data without being processed again**




**Workflow**
1. New CSV files are placed in the raw_data directory
2. The application reads and processes the source data
3. Cleaned and transformed datasets are saved to the clean_data directory
4. Successfully processed source files are moved to the processed_data directory
5. Archived files are excluded from future processing runs, preventing duplicate data handling