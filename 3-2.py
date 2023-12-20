import pandas as pd
file = pd.read_csv("edu_bigdata_imp1.csv", encoding=("big5"), low_memory=False)
filtered_file_2 = file[file["PseudoID"]  == 71]
start = filtered_file_2["dp001_review_start_time"].unique()
end = filtered_file_2["dp001_review_end_time"].unique()
startDate = pd.to_datetime(start)
endDate = pd.to_datetime(end)
result1 = startDate.strftime("%Y-%m-%d")
result2 = endDate.strftime("%Y-%m-%d")

a = result1.unique()
b = result2.unique()
res = (a.union(b)).unique()
for i in range(len(res)):
    print(res[i])