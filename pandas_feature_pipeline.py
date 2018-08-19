import pandas as pd
import numpy as np

a = pd.DataFrame({'A1':[[0,3], [2,3], [3,4]], 'B2':[[1], [22], [3]], 'C3':[3, 4, 5]})
columns_A1 = []
print(a)

## 将一列中的list转换成dataframe中的多列
def one_list_column_to_mutiply_columns(df, columns= []):
    for column in columns:
        if type(df[column][0]) != list:
            continue
        column_size = len(list(df[column][0]))
        if(column_size>0):
            bias_column = [ column + '_' + str(i) for i in range(column_size)]
            df = df.drop(column, axis=1).join(pd.DataFrame(list(df[column]), columns= bias_column))
    return df

a = one_list_column_to_mutiply_columns(a, a.columns)

print(a)
