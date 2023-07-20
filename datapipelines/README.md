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