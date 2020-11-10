from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/<int:userID>')
def hello(userID):
    return 'The user ID is: {}'.format(escape(userID))

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True, host='127.0.0.1', port=80)