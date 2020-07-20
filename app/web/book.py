'''
视图文件(蓝图)
'''
from flask import Flask
from flask import Blueprint

from helper import is_isbn_or_key
from yushu_book import YuShuBook


web = Blueprint('web', __name__)

#路由
@web.route('/book/search/<q>/<page>')
def search(q, page):
    '''
        q :普通关键字 isbn
        page
    
    isbn isbn13 13个0到9的数字组成
    isbn10 10个0到9的数字组成，含有一些' - '
    '''
    isbn_or_key = is_isbn_or_key(q)
    if is_isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    
    # 序列化
    # API
    return jsonify(result)
    #return json.dumps(result), 200, {'content-type':'appdlication/json'}