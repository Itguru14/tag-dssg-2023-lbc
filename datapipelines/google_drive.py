from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import requests
import pandas as pd
from io import BytesIO
from slugify import slugify

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)
folder_id = '1dN0FsnGGx2ugH1Jzh1QaQzdrOXw-ZXMt' # TAG DSSG 2023 - Data (PII Stripped, v1)
file_list_raw = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
file_list = [{'id': x.get('id', ''), 'title': x.get('title', ''), 'mimeType': x.get('mimeType', '')}
             for x in file_list_raw
             if x.get('mimeType') not in ['application/vnd.google-apps.shortcut', 'application/pdf']]

def list_children_for_parent_id(id):
    return drive.ListFile({'q': f"'{id}' in parents and trashed=false"}).GetList()

def google_drive_file_to_df(gauth, file_id):
    url = f"https://docs.google.com/spreadsheets/export?id={file_id}&exportFormat=csv"
    res = requests.get(url, headers={"Authorization": "Bearer " + gauth.attr['credentials'].access_token})
    df = pd.read_csv(BytesIO(res.content), dtype=str)
    return df

def df_to_bigquery(df, dataset, table, if_exists='replace'):
    df.to_gbq(f'{dataset}.{table}', if_exists=if_exists, project_id='tag-dssg-2023-lbc-all-teams')

# THIS PART NEEDS SOME LOVE
# if __name__ == '__main__':
#     folder_items = list_children_for_parent_id(folder_id)
#     subfolders = [file for file in folder_items if file['mimeType'] == 'application/vnd.google-apps.folder']
#     for subfolder in subfolders:
#         subfolder_slug = slugify(subfolder['title']).upper().replace('-', '_')
#         subfolder_items = list_children_for_parent_id(subfolder['id'])
#         for subfolder_item in subfolder_items:
#             if subfolder_item['mimeType'] == 'application/vnd.google-apps.spreadsheet':
#                 df = google_drive_file_to_df(gauth, subfolder_item['id'])
#                 df_to_bigquery(df, dataset='TAG_DSSG_2023', table=subfolder_slug, if_exists='replace')
