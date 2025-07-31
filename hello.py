from flask import Flask

app = Flask(__name__)
# print(__name__)

def make_bold(func):
    def wrapper():
        return "<b>"+func()+"</b"
    return wrapper

def make_emphasis(func):
    def wrapper():
        return "<em>"+func()+"</em>"
    return wrapper

def make_underlined(func):
    def wrapper():
        return "<u>"+func()+"</u"
    return wrapper

@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph written in PyCharm.</p>'
            '<p>Please enjoy this GIF of Jiji from Kiki&#39;s Delivery Service</p>'
            '<img src="https://pa1.aminoapps.com/6241/7c70e19703679f9a46690c1349f5a1e2324a29ee_hq.gif" width=400>')

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!'

# Uses Variable Rules from Flask Doc
# <number> uses converter to type cast str -> int
@app.route('/username/<name_variable>/<int:number>')
def greet(name_variable, number):
    return f"Hello {name_variable}! You are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)
# Turns Debugger On!
