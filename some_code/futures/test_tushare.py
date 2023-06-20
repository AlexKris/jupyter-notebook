import configparser
import json
from datetime import datetime

import pandas as pd
import tushare as ts

config = configparser.ConfigParser()
config.read('../config/tushare.ini', encoding='utf-8')
token = config.get('tushare', 'token')

pro = ts.pro_api(token)

# 郑州商品交易所
df = pro.fut_basic(exchange='CZCE', fut_type='2')
df = df[~df['name'].str.contains('连续|月|季')]
CZCE_ts_code = df.to_dict('records')
# 上海期货交易所
df = pro.fut_basic(exchange='SHFE', fut_type='2')
df = df[~df['name'].str.contains('连续|月|季')]
SHFE_ts_code = df.to_dict('records')
# 大连商品交易所
df = pro.fut_basic(exchange='DCE', fut_type='2')
df = df[~df['name'].str.contains('连续|月|季')]
DCE_ts_code = df.to_dict('records')
# 中国金融期货交易所
df = pro.fut_basic(exchange='CFFEX', fut_type='2')
df = df[~df['name'].str.contains('连续|月|季')]
CFFEX_ts_code = df.to_dict('records')
# 上海国际能源交易所
df = pro.fut_basic(exchange='INE', fut_type='2')
df = df[~df['name'].str.contains('连续|月|季')]
INE_ts_code = df.to_dict('records')
# 广州期货交易所
df = pro.fut_basic(exchange='GFEX', fut_type='2')
df = df[~df['name'].str.contains('连续|月|季')]
GFEX_ts_code = df.to_dict('records')

df1: pd.DataFrame = None
ts_code_list = []
# 获取主力合约
for ts_code in CZCE_ts_code:
    df = pro.fut_mapping(ts_code=ts_code['ts_code'])
    ts_code_list.append(df.iloc[0].to_dict())

for ts_code in SHFE_ts_code:
    df = pro.fut_mapping(ts_code=ts_code['ts_code'])
    ts_code_list.append(df.iloc[0].to_dict())

for ts_code in DCE_ts_code:
    df = pro.fut_mapping(ts_code=ts_code['ts_code'])
    ts_code_list.append(df.iloc[0].to_dict())

for ts_code in CFFEX_ts_code:
    df = pro.fut_mapping(ts_code=ts_code['ts_code'])
    ts_code_list.append(df.iloc[0].to_dict())

for ts_code in INE_ts_code:
    df = pro.fut_mapping(ts_code=ts_code['ts_code'])
    ts_code_list.append(df.iloc[0].to_dict())

for ts_code in GFEX_ts_code:
    df = pro.fut_mapping(ts_code=ts_code['ts_code'])
    ts_code_list.append(df.iloc[0].to_dict())

ts_code_dict = {}
for ts_code in ts_code_list:
    trade_date = ts_code['trade_date']
    now_date_time = datetime.now().strftime('%Y%m%d')
    if trade_date >= now_date_time:
        mapping_ts_code = ts_code['mapping_ts_code']
        if mapping_ts_code.endswith('.ZCE'):
            # 郑州商品交易所
            ts_code_str = ts_code['ts_code']
            ts_code_str = ts_code_str.replace('.ZCE', '')
            value = 'xzce_' + ts_code_str.lower()
            key = mapping_ts_code.replace('.ZCE', '').replace('23', '3')
            ts_code_dict[key] = value
        elif mapping_ts_code.endswith('.SHF'):
            # 上海期货交易所
            ts_code_str = ts_code['ts_code']
            ts_code_str = ts_code_str.replace('.SHF', '')
            value = 'xsge_' + ts_code_str.lower()
            key = mapping_ts_code.replace('.SHF', '').lower()
            ts_code_dict[key] = value
        elif mapping_ts_code.endswith('.DCE'):
            # 大连商品交易所
            ts_code_str = ts_code['ts_code']
            ts_code_str = ts_code_str.replace('.DCE', '')
            value = 'xdce_' + ts_code_str.lower()
            key = mapping_ts_code.replace('.DCE', '').lower()
            ts_code_dict[key] = value
        elif mapping_ts_code.endswith('.CFX'):
            # 中国金融期货交易所
            ts_code_str = ts_code['ts_code']
            if ts_code_str.startswith('TL0'):
                ts_code_str = ts_code_str.replace('TL0', 'TL')
            ts_code_str = ts_code_str.replace('.CFX', '')
            value = 'ccfx_' + ts_code_str.lower()
            key = mapping_ts_code.replace('.CFX', '').upper()
            ts_code_dict[key] = value
        elif mapping_ts_code.endswith('.INE'):
            # 上海国际能源交易所
            ts_code_str = ts_code['ts_code']
            if ts_code_str.startswith('SCTAS'):
                continue
            ts_code_str = ts_code_str.replace('.INE', '')
            value = 'xine_' + ts_code_str.lower()
            key = mapping_ts_code.replace('.INE', '').lower()
            ts_code_dict[key] = value
        elif mapping_ts_code.endswith('.GFE'):
            # 广州期货交易所
            ts_code_str = ts_code['ts_code']
            ts_code_str = ts_code_str.replace('.GFE', '')
            value = 'gfex_' + ts_code_str.lower()
            key = mapping_ts_code.replace('.GFE', '').lower()
            ts_code_dict[key] = value

with open('data_quote.json', 'w') as f:
    json.dump(dict(sorted(ts_code_dict.items(), key=lambda d: d[1])), f, indent=4)