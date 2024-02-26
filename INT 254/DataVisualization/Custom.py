import pandas as pd
import numpy as np 
df=pd.read_csv("Data.csv")
print(df)
print("----------------------")
#Adding a dummy column of only zeroes
df['zero']=0
print(df)
print("----------------------")
print(df.__len__())
print("----------------------")
df.drop('dummy',axis=1,inplace=True)
print(df)
print("----------------------")
#drop the row
# df=df.drop(2)
# print(df)
print("----------------------")
df.drop(2,inplace=True)
print(df)
df.drop(2,axis=1,inplace=True)
print(df)
