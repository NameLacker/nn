'''
搜索用的API
'''

from Http import HTTP

class YuShuBook:
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
    def search_by_keyword(cls, keyword, count=15, start=0):
        url = cls.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result