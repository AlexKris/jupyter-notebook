import urllib.request
import json

host = 'http://api.cj.le61.cn'
appcode = 'b629ffae8d404953a2768a2ac8e8d8b2'
req_headers = {'Authorization': 'APPCODE ' + appcode}

def query_newest(lastOutId, size):
    path = '/kuaixun/newest'
    querys = ''
    if lastOutId:
        if size :
            querys = f'lastOutId={lastOutId}&size={size}'
        else:
            querys = f'lastOutId={lastOutId}'
    elif size:
        querys = f'size={size}'
    req_url = host + path + '?' + querys
    req = urllib.request.Request(url=req_url, headers=req_headers)
    with urllib.request.urlopen(req) as resp:
        content = resp.read()
    
    return content

if __name__ == '__main__':
    newest = query_newest(None, None)
    # print(newest)
    newest_json = json.loads(newest)
    for newest_obj in newest_json:
        print(newest_obj)