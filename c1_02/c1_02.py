#-*- encoding=UTF-8 -*-
#python装饰器 和 Java注解相似

from flask import Flask, \
    render_template, request, make_response,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route('/profile')
@app.route('/profile/<int:uid>')
def profile(uid):
    return render_template('profile.html', uid=uid)

@app.route('/request')
def request_demo():
    res = ''
    for property in dir(request):
        res = res+str(property)+'<br>' + str(eval('request.'+property))
    return res

def log(func):
    def wrapper():
        print 'before calling', func.__name__
        func()
        print 'end calling', func.__name__
    return wrapper

@log
def hello():
    print 'Hello'

@app.route('/testredirect')
def redirct_demo():
    return redirect('profile.html',)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html',url = request.url)

@app.route('/admin')
def admin():
    key = request.args.get('key')
    if key == 'admin':
        return 'hello admin'
    else:
        raise Exception()
    return 'XX'

if __name__ == '__main__':
    app.run(debug=True)

#支持幂等性的POST