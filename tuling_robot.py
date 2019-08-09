# http://www.turingapi.com

# 步骤：
# 1、注册或登录
# 2、创建应用，获取 APIKEY
# 3、发送问题
# 4、返回答案
import json

import requests

key = 'eac72b03fb4e4bc789d8ba8067c94f33'
while True:
    url = 'http://www.tuling123.com/openapi/api?key='+key+'&info='+input('我：')
    resp = requests.get(url)
    data = json.loads(resp.text)
    print('机器人：'+data['text'])