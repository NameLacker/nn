'''
主函数
'''
from app.__init__ import create_app


app = create_app()


if __name__ == "__main__":
    print(id(app))
    # 生产环境 nginx+uwsgi
    app.run(host=app.config['HOST'], debug=app.config['DEBUG'], port=app.config['PORT'])
