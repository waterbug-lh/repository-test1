import pandas as pd
import numpy as np

"""
df=pd.read_csv("data/ru9999_1h.csv",nrows=5)
print("列名:",df.columns.tolist())
print(df.head())
"""

df=pd.read_csv("data/ru9999_1h.csv",
               parse_dates=["datetime"],
               index_col="datetime")

print("前五行")
print(df.head(),"\n")

print("=== 信息概要 ===")
print(df.info(),"\n")

#按日期切片
df_arpil29=df.loc["2025-04-29"]
print(df_arpil29)
df_range=df.loc["2025-05-01 00:00":"2025-05-06 15:00"]
print(df_range)

#条件过滤
df_high=df[df["high"]>16000]
print("最高价大于16000:",df_high)
print(df_high.head())
#组合条件
df_combo=df[(df["high"]>16000)& (df["low"]<15900)]
print("组合条件：high>16000 & low<15900",df_combo)

#按日计算平均收盘价
df_AvgClose=df["close"].resample("D").mean()
print("按日计算平均收盘价:（前五天）",df_AvgClose.head())
#按周计算成交量总和
df_SumVolume=df["volume"].resample("W").sum()
print("按周计算总成交量:",df_SumVolume)

#用numpy计算
df_arr=df["close"].values
print("平均收盘价:",np.mean(df_arr))
print("收盘价方差:",np.std(df_arr))

