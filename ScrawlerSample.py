from flask import Flask
import requests

app = Flask(__name__)


@app.route('/getInfo')
def hello_world():
    if (str(headers.get('User-Agent')).startswith('python')):
        return "小子,使用爬虫是吧?"
    else:
         return "这里假装有很多数据"


if __name__ == "__main__":
    app.run(debug=True)
