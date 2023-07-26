## Setup Instructions

`google_drive.py`

### Google Cloud

1. Open Google Cloud Platform: console.cloud.google.com
1. Select project: `tag-dssg-2023-lbc-all-teams` (Brent Brewington can add you on request)
1. Enable Google Drive API (in API's & Services --> Enable --> Google Drive)
1. Create Credentials
1. Oauth Client ID
1. Application Type = "Desktop App"
1. Download JSON
1. Copy contents of JSON into `client_secrets.json` (and recommend deleting the original file)

When you run code in `datapipelines/google_drive.py`, it will use the JSON file from the last step and will confirm if it's valid

### Local Environment

In command line (like bash or zsh):

```bash
cd datapipelines
source setup.sh
```

## Automated Data Extraction

"03_gdrive_file_id_list.py"

This script "03_gdrive_file_id_list.py" will list all of the files and folders in your google drive so you may see the data folder saved in your google drive that you wantb to pull. you need to set up your google drive api credentials on google cloud and save the
resulting credential file as credentials.json in the present working directory with that done the script would gave access to you google drive.

"04_gdrive_to_local.py"

This script should pulls the require data from google drive using the specified
id in folder_id. it uses the zdrive module which must be installed before you are able to use the script. Please replace the folder_id with the id corresponding to the data folder TAG DSSG 2023 - Data (PII Stripped, v1), you can obtain the required folder id by running the script "03_gdrive_file_id_list.py" which lists all the ids and corresponding names of all files and folders on your google drive so you can pick the Id corresponding
to TAG DSSG 2023 - Data (PII Stripped, v1). the pulled data will be saved in a folder named 'drive_content'



## Data Transformation and PreProprocessing.

Typically in most Data anlysis endeavors the original data available for analysis is never in an ideal state that can just be used for the analysis, hence the term messy data which is a term synonymous with data  that can not be used to carry out required analysis without some form of data transformation aimed at improving the quality of the data before any analysis is done. To this end we would carry out a few simple transformations on the available data for this project. The first transformaation is a data aggregation operation aimed at merging several files of the given dataset into fewer files so as to be able to have all necessary data in one place for the purpose of analysis. The second transformation is to remove columns in data files that may offer little to no value in other to make the data more manageable. To carry out this two transformnation we use the py scripts in The subfolder named "datapipelines" in this directory. The scripts outputs a single csv file for each for subfolder in the main data folder containing several .xlsx or csv files the single csv file contain all the aggregated data from seven all of the files in each folder stcked together.


The following files in this repos is intended to be used to transform and clean our original data. Please find below what each file does and how to use it you may also find helpful comments in the actual files.

square-items-details-stack.py    ( intended to be used to stack up all the files in the subfolder named Square-Item-Details-PII-Stripped ) it stacks all of the xlsx files in the                                    directory and removes all empty columns, the output of the file is a csv file.

square-items-sales-summary-stack.py    same function as above but for the second subfolder in the main data folder

square-transactions-stack.py           Same as above  but for the third subfolder in the main data folder

data-cleansing.py                      This file is used to readin csv file output from above file and then replaces non-muneric values in columns
                                       that are supposed to be numeric in value with NaNs/Null

Salesforce-Opportunity -2023-07-07.py     same function as above file but for the Salesforce-Opportunity-2023-07-07.xlsx file                                      

                                  
Item_Catalog.py                           same function as above but for the square_item_catalog.xlsx file 





