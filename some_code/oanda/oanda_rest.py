import json

import requests
from oanda_config import OandaConfig

oandaConfig = OandaConfig()
token = oandaConfig.token

request_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
}
hostname = oandaConfig.hostname
requets_url = f'https://{hostname}'
streaming_hostname = oandaConfig.streaming_hostname
requets_stream_url = 'https://{streaming_hostname}'
request_param = {
    'instruments': 'XAG_USD'
}
active_account = oandaConfig.active_account
resp = requests.get(
    url=requets_stream_url+f'/v3/accounts/{active_account}/pricing/stream',
    headers=request_headers,
    params=request_param
)
if resp.status_code == 200:
    print('请求成功')
else:
    print('请求失败')
print(resp.text)
