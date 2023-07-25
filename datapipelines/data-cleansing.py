import pandas as pd
import re
import os
import glob
import numpy as np
import pathlib
from pathlib import Path
#import Path



x=pd.read_csv("square-items-details-stack.csv")

#print(x)

#x.loc[1001, "Gross Sales"]=0

#print(x.loc[1001, "Gross Sales"])

for i in range(0, len(x)):

      k1=x.loc[i, "Gross Sales"]
      k2=x.loc[i, "Net Sales"]

      if isinstance(k1, int) is False and isinstance(k1, float) is False:
             
               x.loc[i, "Gross Sales"] = np.nan

      if isinstance(k2, int) is False and isinstance(k2, float) is False:

               x.loc[i, "Net Sales"] = np.nan

      
x.to_csv('square-items-details-stack.csv', index=False)     

print(x)




# print(isinstance(f_i, int))
# # False

# print(isinstance(f_i, float))
# # True


