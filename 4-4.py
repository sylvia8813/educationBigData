import pandas as pd
file = pd.read_csv("edu_bigdata_imp1.csv", encoding=("big5"), low_memory=False)
filtered_file_1 = file[file["dp002_extensions_alignment"] == '["校園職業安全"]']
print(len(filtered_file_1))