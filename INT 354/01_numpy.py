import pandas as pd
from io import StringIO
csv_data = '''A,B,C,D
1.0,2.0,3.0,4.0
5.0,6.0,99.0,8.0
10.0,11.0,12.0
32.0,,22.0
43.0,,2.0'''

df=pd.read_csv(StringIO(csv_data))
print(df)
print("------------------------------------")
print(df.values)
print("------------------------------------")
print(df.dropna(axis=0)) #Delete full row for NaN
print("------------------------------------")
print(df.dropna(axis=1)) #Delete full coloumn for NaN
print("------------------------------------")
print(df.isnull().sum())
print("------------------------------------")

#The above methods delete full row or coloumn.To avoid we use simpleimputer

from sklearn.impute import SimpleImputer
import numpy as np
#imr=SimpleImputer(missing_values=np.nan,strategy='most_frequent')
#imr=SimpleImputer(missing_values=np.nan,strategy='mean')
imr=SimpleImputer(missing_values=np.nan,strategy='median')
imr=imr.fit(df.values)
imputed_data=imr.transform(df.values)
print(imputed_data)
print("------------------------------------")
df1=pd.DataFrame(imputed_data,index=["0","1","2","3","4"],columns=["a","b","c","d"])
print(df1)
print("------------------------------------")

# print(df.fillna(df.mean()))
# print(df.fillna(df.median()))
