from flask import Flask

app = Flask(__name__)
# print(__name__)

@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph written in PyCharm.</p>'
            '<p>Please enjoy this GIF of Jiji from Kiki&#39;s Delivery Service</p>'
            '<img src="https://pa1.aminoapps.com/6241/7c70e19703679f9a46690c1349f5a1e2324a29ee_hq.gif" width=400>')

@app.route('/bye')
def bye():
    return 'Bye!'

@app.route('/username/<name>/<int:number>')  # <> becomes a variable
def greet(name, number):
    return f"Hello {name}! You are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)
