import tushare as ts

pro = ts.pro_api('98a130211463d3a7e82b07dc8e4af1b4cb1c6a0431c1f070c6dafd42')
data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
with open('stock_basic.txt', 'w') as file_object:
    for data_str in data.values.tolist():
        print(data_str)
        print("join" + ",".join(data_str))
        file_object.write(",".join(data_str) + "\n")