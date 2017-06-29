# encoding: utf-8
from flask import Flask
from flask import render_template

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
app = Flask(__name__)


@app.route('/')
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

    ]
    return render_template('index.html',infos=infos,links=links)


if __name__ == '__main__':
    app.run(debug=True)
