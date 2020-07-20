'''
功能模块
'''

#判断是isbn10还是isbn13(isbn)
def is_isbn_or_key(q):
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    #去掉'-'
    short_q = q.replace('-', '')
    if '-' in q and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn10'
    
    return isbn_or_key

