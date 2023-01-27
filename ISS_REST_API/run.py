from flask import Flask
from iss import query

app = Flask(__name__)

@app.route('/')
def index():
    ret = query()
    ret = f'json: {ret["json"]} --- text: {ret["text"]}'
    return ret

@app.route('/json')
def json():
    ret = query()
    return ret['json']

@app.route('/text')
def text():
    ret = query()
    return ret['text']

if __name__ == '__main__':
    app.run()