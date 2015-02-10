import json
from bottle import route, run, template
from bottle import static_file
from bottle import get, post, request

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/static')
def static():
    return static_file('test.html', root='./')

@route('/post', method='post')
def post():
    jsn = request.forms.get('json')
    o = json.loads(jsn)
    return o['func']

run(host='0.0.0.0', port=80, server='cherrypy')
