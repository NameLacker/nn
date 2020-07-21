'''
搜索用的API
'''

from app.libs.Http import HTTP
from flask import current_app
from fisher import app

class YuShuBook:
    # 模型层 MVC M层
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'
    
    @classmethod
    def search_by_isbn(cls, isbn):
        # format 格式化
        url = cls.isbn_url.format(isbn)
        #获得json格式的文件
        result = HTTP.get(url)
        return result
    
    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PRE_PAGE'], calculate_start(page))
        result = HTTP.get(url)
        return result
    
    @staticmethod
    def calculate_start(page):
        return (page-1)*current_app.config['PRE_PAGE']