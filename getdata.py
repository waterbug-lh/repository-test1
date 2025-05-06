import akshare as aks

#dfmap=aks.futures_display_main_sina()
#print(dfmap.head)

df = aks.futures_zh_minute_sina(symbol="RU0",period="60")
df.to_csv("data/ru9999_1h.csv",index=False)