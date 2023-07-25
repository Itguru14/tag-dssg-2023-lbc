import pandas as pd
import re
import os
import glob
import numpy as np
import pathlib
from pathlib import Path
#import Path

# you must change cwd to where this file is located to run this filels

flist = []
for p in pathlib.Path('.').iterdir():
    if p.is_file():
        print(p)
        flist.append(p)
print(flist)

df = pd.DataFrame()
new_df=pd.DataFrame()
for f in flist:

     if  Path(f).suffix == '.xlsx':
        new_df=pd.read_excel(f)
        df= pd.concat([df,new_df])

#print(df)
     
print(df.shape)

#Discounts
#Net Sales
#Tax

#Amount
#Job_Location_Zip__c

deletion_threshhold=1                              #removes all columns in the dataframe with proportion of empty values greater than threshold
df = df.loc[:, df.isin([' ','NULL', np.nan]).mean() != deletion_threshhold]    #may include whatever signify 'empty'


# x=df.loc[1000, "Gross Sales"]
# print(x)




print(df.shape)


df.to_csv('square-items-details-stack.csv', index=False)     



