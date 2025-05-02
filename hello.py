from flask import Flask

app = Flask(__name__)
# print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def bye():
    return 'Bye!'

@app.route('/username/<name>/<int:number>')  # <> becomes a variable
def greet(name, number):
    return f"Hello {name}! You are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
