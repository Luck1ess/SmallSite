import os
from bottle import route, run, static_file

@route('/question65')
def server_static():
    return static_file("question65.html", root=os.path.join(os.getcwd(), "src/"))

run(host='localhost', port=8080)