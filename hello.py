from flask import Flask

app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def bye():
    return 'Bye!'

def greet(name):
    ...

if __name__ == "__main__":
    app.run()

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
