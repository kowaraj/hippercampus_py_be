from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "login POST"
    else:
        return "login GET"

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print(request.files)
    f = request.files.get('sampleFile')
    print(f)
    tags = request.form.get('tags')
    print(tags)    
    print(request.args)
    if request.method == 'POST':
        return "upload POST"
    else:
        return "upload GET"
