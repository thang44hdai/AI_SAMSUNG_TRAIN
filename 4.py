import pandas as pd
import numpy as np

data = pd.read_csv("P4AI_BT1.csv")

df1 = data.copy()
df1['sepal.length'].fillna(round(data['sepal.length'].mean()),inplace=True)
df1['sepal.width'].fillna(round(data['sepal.width'].mean()),inplace=True)
df1['petal.length'].fillna(round(data['petal.length'].mean()),inplace=True)
df1['petal.width'].fillna(round(data['petal.width'].mean()),inplace=True)

df3 = df1.copy()
sepal_length_max = df3["sepal.length"].max()
sepal_length_min = df3["sepal.length"].min()
sepal_width_max = df3["sepal.width"].max()
sepal_width_min = df3["sepal.width"].min()
petal_length_max = df3["petal.length"].max()
petal_length_min = df3["petal.length"].min()
petal_width_max = df3["petal.width"].max()
petal_width_min = df3["petal.width"].min()

df3['sepal.length'] = (df3['sepal.length'] - sepal_length_min)/(sepal_length_max - sepal_length_min)
df3['sepal.width'] = (df3['sepal.width'] - sepal_width_min)/(sepal_width_max - sepal_width_min)
df3['petal.length'] = (df3['petal.length'] - petal_length_min)/(petal_length_max - petal_length_min)
df3['petal.width'] = (df3['petal.width'] - petal_width_min)/(petal_width_max - petal_width_min)

print(df3)
