from flask import Flask, render_template, request

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

@app.route("/about")
def display():
    Page_title = "Informite-About"
    return render_template("About.html", title=Page_title)

@app.route("/")
def Names():
    Page_title="Informite"
    return render_template("Trial.html", title=Page_title)

if __name__=="__main__":
    app.run(debug=True)
