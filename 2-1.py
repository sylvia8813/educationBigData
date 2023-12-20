import pandas as pd

file = pd.read_csv("edu_bigdata_imp1.csv", encoding=("big5"), low_memory=False)
filtered_file = file[file["PseudoID"] == 281]
filtered_file_1 = filtered_file.dropna(subset = ["dp001_video_item_sn"])
result1_0 = filtered_file_1["dp001_video_item_sn"].unique()
result1_1 = filtered_file["dp001_indicator"].unique()
for i in range(len(result1_0)):
    print(f"{int(result1_0[i])}-->{result1_1[i]}")