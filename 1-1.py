import pandas as pd
file = pd.read_csv("edu_bigdata_imp1.csv", encoding=("big5"), low_memory=False)
filtered_file = file[file["PseudoID"] == 39]
result1 = filtered_file["dp001_review_sn"].unique()
print(len(result1))