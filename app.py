from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/test', methods=['GET'])
def test_endpoint():
    print(request.data)
    print("this is a debug message")
    return "Hello World!"

if __name__ == '__main__':
    app.run()