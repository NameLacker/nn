'''
API
'''

# urllib
#requests
import requests
from urllib import request

#封装成类易于扩展
class HTTP:
    @staticmethod
    def get(url, return_json=True):
        # url: api的地址
        # 返回的是json格式
        r = requests.get(url)
        # restful
        # json
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
    
