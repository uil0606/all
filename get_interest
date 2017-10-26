import pandas as pd
import numpy as np
import math

wd = 'c:/users/magfi/desktop/test (2).xlsx'
df = pd.read_excel(wd)
k = 0
res = pd.DataFrame(columns=['日期', '姓名', '利息'])
df1= df.iloc[:,3:]
for i in range(df1.shape[0]):
    for j in range(0, df1.shape[1]):
        if df1.ix[i,j]==df1.ix[i,j]:
            res.loc[k] = [df1.columns[j], df.iloc[i, 0], df1.iloc[i, j]]
            k += 1
print(res.head(10))
res.to_csv('c:/users/Administrator/desktop/res.csv')
