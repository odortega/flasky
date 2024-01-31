from flask import Flask, request, make_response, redirect,  render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

todos = ['Buy coffee', 'Send request', 'Drink coffee']


app.config.update(
    DEBUG=False,
    ENV='development'
)

# next line sets app config secret key
app.config['SECRET_KEY'] = 'SUPER SECRET'



# class LoginForm
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit  = SubmitField('Submit')

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
    login_form = LoginForm() 
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form
    }
    return render_template('hello.html', **context)

if __name__ == '__main__':
    app.run(port = 5000, debug = True)