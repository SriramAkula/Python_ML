import pandas as pd
data = pd.read_csv("Salaries.csv")
print(data)
print(data.shape)
print(data.head())
print("--------------------------------")
print(data.head(10)) #10 rows
print("--------------------------------")
print(data.tail())
print("--------------------------------")
print(data.tail(10)) # last 10 rows
print("--------------------------------")
print(data.dtypes) # to know data types of columns
print("--------------------------------")
print(data['salary'].dtypes) # to know data types of particular coloumn
print("--------------------------------")

# DataFrames Attributes
# dtypes,coloumns,axes,ndim,size,shape,values
print(data.columns)
print("--------------------------------")
print(data.axes)
print("--------------------------------")
print(data.size)
print("--------------------------------")
print(data[2:4])
print("--------------------------------")

#Data Frames methods
''' head/tail()
    describe()
    max()/min()
    mean / median
    std(): Standard Deviation
    sample([n])
    dropna(): drop records with missing values
'''
print(data.describe())
print("--------------------------------")
df=data.head(50)
print(df.mean(numeric_only=all))
print("--------------------------------")
print(data.head(50).mean(numeric_only=all))
print("--------------------------------")
