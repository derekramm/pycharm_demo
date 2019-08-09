import hashlib
import time
import random
import string
import requests
from urllib.parse import quote

def curlmd5(src):
    m = hashlib.md5(src.encode('UTF-8'))
    return m.hexdigest().upper()

def get_params(content):
    time_stamp = str(int(time.time()))  # 请求时间戳

    # 请求随机字符串，用于保证签名不可预测  
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))

    # 应用标志，这里修改成自己的id和key  
    app_id = '2119609776'
    app_key = 'FsmvyualvLNtnoAf'
    params = None

    params = {'app_id': app_id,
              'question': content,
              'time_stamp': time_stamp,
              'nonce_str': nonce_str,
              'session': '10000'
              }

    sign_before = ''
    # 要对key排序再拼接
    for key in sorted(params):
        # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8。quote默认大写。
        sign_before += '{}={}&'.format(key, quote(params[key], safe=''))
    # 将应用密钥以app_key为键名，拼接到字符串sign_before末尾
    sign_before += 'app_key={}'.format(app_key)
    # 对字符串sign_before进行MD5运算，得到接口请求签名  
    sign = curlmd5(sign_before)
    params['sign'] = sign
    return params

def get_content(question_content):
    # global payload, r
    # 聊天的API地址 
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
    # 获取请求参数  
    question_content = question_content.encode('utf-8')
    params = get_params(question_content)
    r = requests.post(url, data=params)
    return r.json()["data"]["answer"]

if __name__ == '__main__':
    while True:
        question = input('我：')
        if question:
            answer = get_content(question)
            print(f'机器人：{answer}')
        else:
            print('下次再见！')
            break
