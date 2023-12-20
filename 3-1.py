import pandas as pd
file = pd.read_csv("edu_bigdata_imp1.csv", encoding=("big5"), low_memory=False)
filtered_file_1 = file[(file["PseudoID"] == 71) & (file["dp001_record_plus_view_action"] == "paused")]
print(len(filtered_file_1))