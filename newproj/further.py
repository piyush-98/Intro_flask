##It is possible to return the output of a function bound to a certain URL in the form of HTML.
##For instance, in the following script, hello() function will render ‘Hello World’ with <h1> tag attached to it.

from flask import Flask
from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def index():
    return '<html><body><p><b>Generating html code from python is hectic task thats where templates come into play</b></p></body></html>'

## This is where one can take advantage of Jinja2 template engine, on which Flask is based.
## Instead of returning hardcode HTML from the function, a HTML file can be rendered by the render_template() function.

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)

if __name__ == '__main__':
   app.run(debug = True)
