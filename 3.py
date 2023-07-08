import pandas as pd
import numpy as np

data = pd.read_csv("P4AI_BT1.csv")

df1 = data.copy()
df2 = df1[(df1['sepal.length'] > 5) & (df1['sepal.width'] > 3)];

print(df2)

