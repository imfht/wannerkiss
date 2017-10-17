# encoding: utf-8
import sys

from flask import Flask
from flask import render_template

reload(sys)
sys.setdefaultencoding('utf-8')
app = Flask(__name__)
from flask import request
from model import *

db.init_app(app)

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    infos = [u'我喜欢方核桃，我要给她生猴子！', u'楼上好像喜欢方核桃，真不要脸', u'我喜欢鸡公煲同学.我想申请一个 jigongbao.uwillkiss.me',
             u'其实 willkiss.me也不错，不过好像被人注册了..', u'我靠辣鸡站长丧心病狂把willkiss.me 也买了！'
             ]
    links = [{
        'href': 'http://xiaohua.willkiss.me',
        'title': '给牛小花做的表白网站',
        'info': '我想和你一起虚度时光，陪你一起发呆，一起睡觉。',
    },
        {
            'href': 'http://hetao.willkiss.me',
            'title': '给大核桃的情话',
            'info': '情话是我抄的，但只说给你听是真的。 '

        },
        {
            'href': 'http://hetao.willkiss.me',
            'title': '给大核桃的情话',
            'info': '情话是我抄的，但只说给你听是真的。 '

        },
        {
            'href': 'http://hetao.willkiss.me',
            'title': '给大核桃的情话',
            'info': '情话是我抄的，但只说给你听是真的。 '

        },
        {
            'href': 'http://hetao.willkiss.me',
            'title': '给大核桃的情话',
            'info': '情话是我抄的，但只说给你听是真的。 '

        },
        {
            'href': 'http://hetao.willkiss.me',
            'title': '给大核桃的情话',
            'info': '情话是我抄的，但只说给你听是真的。 '

        },
        {
            'href': 'http://hetao.willkiss.me',
            'title': '给大核桃的情话',
            'info': '情话是我抄的，但只说给你听是真的。 '

        },
        {
            'href': 'http://hetao.willkiss.me',
            'title': '给大核桃的情话',
            'info': '情话是我抄的，但只说给你听是真的。 '

        },
        {
            'href': 'http://hetao.willkiss.me',
            'title': '给大核桃的情话',
            'info': '情话是我抄的，但只说给你听是真的。 '

        }
    ]
    others = [{
        'href': 'http://xiaohua.willkiss.me',
        'title': '嘿，牛小姐',
        'info': '今天穿得很漂亮哦~',
    },
        {
            'href': 'http://hetao.willkiss.me',
            'title': '嘿，牛小姐我今天又看到你了',
            'info': '电脑慢一点话，我就能用编译代码的时间来找你聊天了。'
        },
    ]
    if request.method == 'POST':
        title = request.form.get('title')
        text = request.form.get('text')
        db.session.add(Post(title=title, text=text))
    return render_template("index.html", others=Post.query.order_by(Post.id.desc()).all())


if __name__ == '__main__':
    db.create_all(app=app)
    app.run(debug=True)
