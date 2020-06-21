from flask import Flask, render_template

app = Flask(__name__)

# @ signifies a decorator - way to wrap a funtion and modifying its behaviour
"""
Comments
"""""""""""""""""""""""""""""""""""""""""""""""""
Everytime you open the website , the default will
appear bu this funtion
 |
\|/
"""""""""""""""""""""""""""""""""""""""""""""""""
@app.route("/")
def index():
    return "Hello, world!"
""""""""""""""""""""""""""""""""""""""""""""""""
After the default route, what follows is this
 |
\|/
""""""""""""""""""""""""""""""""""""""""""""""""
@app.route("/david")
def david():
    return "Hello, David"

@app.route("/<string:name>")
def Yourname(name):
    name = name.capitalize()
    return "<h1><center>Hello, {}!</center></h1>".format(name)
"""
#@app.route("/")
#def index():
#    Page_title = "RESPONSE"
#    return render_template("Responsive.html", names = [],title=Page_title, Header="THIS IS SAMPLE")

@app.route("/bye")
def display():
    Page_title = "RESPONSE"
    return render_template("First.html", title=Page_title)

@app.route("/")
def Names():
    Page_title = "RESPONSE"
    names = ["Python", "Java", "Javascript"]
    return render_template("Responsive.html", names = names, title=Page_title, Header = "Just Checking")

if __name__=="__main__":
    app.run(debug=True)
