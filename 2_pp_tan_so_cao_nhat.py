import pandas as pd
import numpy as np

data = pd.read_csv("P4AI_BT1.csv")
df1 = data.copy()

# Tiến hành thay giá trị 'NaN' bằng giá trị trung bình
#fillna: Hàm điền giá trị NaN
#mode: Hàm lấy giá trị có tần số xuất hiện lớn nhất
df1['sepal.length'].fillna(df1['sepal.length'].mode()[0], inplace = True)
df1['sepal.width'].fillna(df1['sepal.width'].mode()[0], inplace = True)
df1['petal.length'].fillna(df1['petal.length'].mode()[0], inplace = True)
df1['petal.width'].fillna(df1['petal.width'].mode()[0], inplace = True)

print(df1.isna().sum())

