import pandas as pd
import re

import os

import glob







files_list = []
print("Using glob.glob()")
files = glob.glob('TAG DSSG 2023 - Data (PII Stripped, v1)/**/*.xlsx', 
                   recursive = True)
# for file in files:
#     print(file)


print(files[1])
filename=files[1]
df = pd.read_excel(files[1])
print(df.columns)


def mask_id(id):
    return re.sub(r'\b[A-Za-z0-9]+\b', '########', id)

# def mask_name(Name):
#     return re.sub(r'\b[A-Za-z0-9]+\b', '########', Name)

     
# def mask_address(Address):
#     return re.sub(r'\b[A-Za-z0-9]+\b', '########', Address)


# def mask_phone_number(phone_number):
#     return re.sub(r'\b[+0-9]+\b', '########', phone_number)



# df['Name'] = df['Name'].apply(mask_name)

# df['Address'] = df['Address'].apply(mask_address)

# df['Phone Number'] = df['Phone Number'].apply(mask_address)


df['Id'] = df['Id'].apply(mask_id)

print(df)
print(filename)

k=filename.split('\\')

df.to_excel('out.xlsx')  


# def mask_email(email):
#     return re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'xxxxx@xxxxx.com', email)

# df['Email'] = df['Email'].apply(mask_email)









