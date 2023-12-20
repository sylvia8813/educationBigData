import pandas as pd

file = pd.read_csv("edu_bigdata_imp1.csv", encoding="big5", low_memory=False)
filtered = file.dropna(subset = ["dp001_review_sn"])
max = filtered["dp001_review_sn"].value_counts() #計算次數
print(int(max.idxmax())) #找到次數最大的
print(max.max())
