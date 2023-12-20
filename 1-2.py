import pandas as pd
file = pd.read_csv("edu_bigdata_imp1.csv", encoding=("big5"), low_memory=False)
filtered_file = file[file["PseudoID"] == 39]
filtered_file = filtered_file.dropna(subset = ["dp001_question_sn"])
result2 = filtered_file["dp001_question_sn"].unique()
print(len(result2))