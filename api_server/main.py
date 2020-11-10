from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/index')
def index():
    return 'Index Page'


@app.route('/test')
def test():
    return 'Test Page'

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, host='127.0.0.1', port=80)
