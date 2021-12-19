from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "world")
    return f'Hello, {escape(name)}! Greetings from a container'

app.run(host='0.0.0.0', port=5000)