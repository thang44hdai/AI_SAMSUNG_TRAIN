import pandas as pd
import numpy as np

#Bài 1:
data = pd.read_csv("P4AI_BT1.csv")
print(data)

#Bài 2:

#Phương pháp trung bình
df1 = data.copy()
# Tiến hành thay giá trị 'NaN' bằng giá trị trung bình
#fillna: Hàm điền giá trị NaN
#mode: Hàm lấy giá trị có tần số xuất hiện lớn nhất
df1['sepal.length'].fillna(df1['sepal.length'].mode()[0], inplace = True)
df1['sepal.width'].fillna(df1['sepal.width'].mode()[0], inplace = True)
df1['petal.length'].fillna(df1['petal.length'].mode()[0], inplace = True)
df1['petal.width'].fillna(df1['petal.width'].mode()[0], inplace = True)
print(df1.isna().sum())

#Phương pháp tần số cao nhất
df1 = data.copy()
# Tiến hành thay giá trị 'NaN' bằng giá trị trung bình
#fillna: Hàm điền giá trị NaN
#mode: Hàm lấy giá trị có tần số xuất hiện lớn nhất
df1['sepal.length'].fillna(df1['sepal.length'].mode()[0], inplace = True)
df1['sepal.width'].fillna(df1['sepal.width'].mode()[0], inplace = True)
df1['petal.length'].fillna(df1['petal.length'].mode()[0], inplace = True)
df1['petal.width'].fillna(df1['petal.width'].mode()[0], inplace = True)
print(df1.isna().sum())

#Bài 3:
df2 = df1[(df1['sepal.length'] > 5) & (df1['sepal.width'] > 3)];
print(df2)

#Bài 4:
df2 = df1.copy()
sepal_length_max = df2["sepal.length"].max()
sepal_length_min = df2["sepal.length"].min()
sepal_width_max = df2["sepal.width"].max()
sepal_width_min = df2["sepal.width"].min()
petal_length_max = df2["petal.length"].max()
petal_length_min = df2["petal.length"].min()
petal_width_max = df2["petal.width"].max()
petal_width_min = df2["petal.width"].min()

df2['sepal.length'] = (df2['sepal.length'] - sepal_length_min)/(sepal_length_max - sepal_length_min)
df2['sepal.width'] = (df2['sepal.width'] - sepal_width_min)/(sepal_width_max - sepal_width_min)
df2['petal.length'] = (df2['petal.length'] - petal_length_min)/(petal_length_max - petal_length_min)
df2['petal.width'] = (df2['petal.width'] - petal_width_min)/(petal_width_max - petal_width_min)

print(df2)


#Bài 5:
df3 = df2.copy()
df3['variety'].unique()
dummies = pd.get_dummies(df3['variety'])
df3 = pd.concat([df3,dummies], axis=1)
df3.drop('variety', axis=1, inplace=True)

#Bài 6:
df4 = df3.copy();
df4['sepal.length'] = pd.cut(df4["sepal.length"],
       bins=[-0.1, 0.2, 0.4, 0.6, 0.8, 1],
       labels=["Very Short", "Short", "Medium", "Long", "Very Long"])
print(df4)


#Bài 7:
num_sample = int(df4.shape[0] / 2);
df5 = df4.sample(num_sample, replace = True);
pd.set_option('display.max_rows', None); # Không giới hạn số hàng khi hiển thị dữ liệu
print(df5)


