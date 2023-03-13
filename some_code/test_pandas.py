import pandas as pd

# 创建一个时间序列数据框
df = pd.DataFrame({'value': [1, 2, 3, 4, 5]},
                  index=pd.date_range('2022-02-15 13:31:00', periods=5, freq='T'))

print(df)

# 将数据框转换为5分钟级数据
df_5min = df.resample('5T').agg

# 将时间戳向后移动5分钟
df_5min.index = df_5min.index.shift(5, freq='T')

# 输出结果
print(df_5min)