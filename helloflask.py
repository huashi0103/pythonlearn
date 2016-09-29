from flask import Flask
from flask import request
from flask import male_response
from

app=Flask(__name__)

@app.route('/')
def index():
    #return '<h1>Bad Rquest</h1>',400
    response=make_response('<h1>this document carries a cookie</h1>')
    response.set_cookie('answer','42')
    return response
    '''
    user_agent=request.header.get('User-Agent')
    return '<p>Your browser is %s</p>'%user_agent
    '''

@app.route('/user/<name>')
def user(name):
    return '<h1>hello,%s!</h1>'%name
if __name__=='__main__':
    app.run()
