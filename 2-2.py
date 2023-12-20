import pandas as pd
file = pd.read_csv("edu_bigdata_imp1.csv", encoding=("big5"), low_memory=False)
filtered_file_2 = file[(file["PseudoID"] == 281) & (file["dp001_prac_score_rate"] == 100)]
print(len(filtered_file_2))