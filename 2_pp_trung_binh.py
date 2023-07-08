import pandas as pd
import numpy as np

data = pd.read_csv("P4AI_BT1.csv")
df1 = data.copy()

# Tiến hành thay giá trị 'NaN' bằng giá trị trung bình
#fillna: Hàm điền giá trị NaN
#mean: Hàm lấy giá trị trung bình
df1['sepal.length'].fillna(round(data['sepal.length'].mean()),inplace=True)
df1['sepal.width'].fillna(round(data['sepal.width'].mean()),inplace=True)
df1['petal.length'].fillna(round(data['petal.length'].mean()),inplace=True)
df1['petal.width'].fillna(round(data['petal.width'].mean()),inplace=True)

print(df1.isna().sum())

