from flask import Flask, request, make_response, redirect

app = Flask(__name__)

# route function to save the user IP into a cookie
@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    return f'Hello World Flask, your IP is {user_ip}'

if __name__ == '__main__':
    app.run(port = 5000, debug = True)