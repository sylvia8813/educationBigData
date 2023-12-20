import pandas as pd
file = pd.read_csv("edu_bigdata_imp1.csv", encoding="big5", low_memory=False)
dp = file[file["dp002_extensions_alignment"] == '["十二年國民基本教育類"]']
print(len(dp))