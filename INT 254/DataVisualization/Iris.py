import pandas as pd
data=pd.read_csv("Iris.csv")
print(data)
print("--------------------")
df1=pd.get_dummies(data['Species'])
df=pd.concat([data,df1],axis=1)
df.drop(df['Species'],axis=1,inplace=True)
print(df)