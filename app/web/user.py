from flask import Blueprint

# user = Blueprint('user', __name__)

from . import web

@web.route('/url')
def login():
    pass