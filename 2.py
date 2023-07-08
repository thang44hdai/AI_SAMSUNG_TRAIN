import pandas as pd
import numpy as np

data = pd.read_csv("P4AI_BT1.csv")
df1 = data.copy()
print(df1.isna().sum())
