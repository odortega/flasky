from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    user_ip = request.remote_addr
    return f'Hello World Flask, your IP is {user_ip}'

if __name__ == '__main__':
    app.run(port = 5000, debug = True)