from flask import Flask
from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/grading_system')
def system():
    return render_template('auto.html')
@app.route('/grade',methods = ['POST', 'GET'])
def grade():
    if request.method == 'POST':
        result = request.form
        print(type(result['ans']))
        return (result['ans'])


if __name__ == '__main__':
   app.run(debug = True)
