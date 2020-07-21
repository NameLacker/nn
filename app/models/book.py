import json
from sqlalchemy import Column, String
from sqlalchemy import Integer
from flask_sqlalchemy import SQLAlchemy
#from app.models.base import Base


db = SQLAlchemy()

class Book(db):
    """
        一些属性定义重复性比较大，元类可以解决这个问题
    """
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # 书名
    title = Column(String(50), nullable=False)
    # 作者
    _author = Column('author', String(30), default='未名')
    # 精装还是平装
    binding = Column(String(20))
    # 出版社
    publisher = Column(String(50))
    # 价格
    price = Column(String(20))
    # 页数
    pages = Column(Integer)
    # 出版年月
    pubdate = Column(String(20))
    # unique 限制isbn唯一
    isbn = Column(String(15), nullable=False, unique=True)
    # 书籍简介
    summary = Column(String(1000))
    # 图片
    image = Column(String(50))
'''
    @property
    def author(self):
        return self._author if not self._author else json.loads(self._author)

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            self._author = json.dumps(value, ensure_ascii=False)
        else:
            self._author = value

    @property
    def author_str(self):
        return '' if not self._author else '、'.join(self.author)
        '''