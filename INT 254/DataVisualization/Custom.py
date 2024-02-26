import pandas as pd
import numpy as np 
df=pd.read_csv("Data.csv")
print(df)
print("----------------------")
#Adding a dummy column of only zeroes
df['zero']=0
print(df)
print(df.__len__())
