from flask import Flask
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


if __name__ == '__main__':
   app.run(debug = True)## run() helps to run the application and the debug mode relaods the changes automatically the reloading the website,
