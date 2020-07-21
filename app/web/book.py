'''
视图文件(蓝图)
'''
from flask import Flask, request, jsonify
from flask import Blueprint
from app.forms.book import SearchForm

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web


#路由
@web.route('/book/search/<q>/<page>')
def search(q, page):
    '''
        q :普通关键字 isbn
        page
        

    isbn isbn13 13个0到9的数字组成
    isbn10 10个0到9的数字组成，含有一些' - '

    Request Response
    HTTP的请求信息
    查询参数 POST参数 remote ip
    '''
    q = request.args['q']
    page = request.args['page']

    # 参数验证
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if is_isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        # 序列化
        # API
        return jsonify(result)
    else:
        return jsonify(({'msg':'参数校验失败'}))
