import pandas as pd
file = pd.read_csv("edu_bigdata_imp1.csv", encoding="big5", low_memory=False)
filtered = file.dropna(subset = ["dp002_verb_display_zh_TW"])
count = filtered["dp002_verb_display_zh_TW"].value_counts()
res = res = ','.join(count.nlargest(3).index)
print(res)