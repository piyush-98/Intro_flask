from flask import Flask
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/') ## routing the homepage url
def hello_world():
   return "Hello World!!" ## returning string

@app.route("/2ndpage") ## this will be the url for this page (next_page)
def next_page():
   return "you have reached the 2nd page"

@app.route('/2ndpage/<name>') ## DYNAMIC url <variable> which gets its value DYNAMICALLY
def hello_name(name): ## parameter
   return 'hey!! %s!' % name ## string returned

@app.route("/blog") ## blog page
def blog_page():
   return "which blog you'd read"

@app.route("/blog/<int:blogid>") ## DYNAMIC page parameter (integer)
def blog_id(blogid):
   return "welcome to the blog %d" %blogid

## The URL rules of Flask are based on Werkzeug’s routing module. This ensures that the URLs formed are unique and based on precedents laid down by Apache.

@app.route('/python/') ## The ('/') at the end is used for canonical url that means (/python and /python/ will redirect to the same page)
def hello_python():
   return 'Hello Python' ## however /2ndpage will invoke the func next_page() while /2mdpage/ will invoke an error 404.

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))


if __name__ == '__main__':
   app.run(debug = True)## run() helps to run the application and the debug mode relaods the changes automatically the reloading the website,
