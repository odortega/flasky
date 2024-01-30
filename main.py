from flask import Flask, request, make_response, redirect,  render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

todos = ['Buy coffee', 'Send request', 'Drink coffee']


app.config.update(
    DEBUG=False,
    ENV='development'
)

# next line sets app config secret key
app.config['SECRET_KEY'] = 'SUPER SECRET'



# error handler function for 404 error
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error = error)


# error handler function for 500 error
@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error = error)

# route function to save the user IP into a cookie
@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    #response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip
    return response

@app.route('/hello')
def hello():
    #user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    return render_template('hello.html', **context)

if __name__ == '__main__':
    app.run(port = 5000, debug = True)