from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


counter = 0

@app.route('/', methods=['GET'])
def index():
    return "Welcome to the counter app! The current count is: " + str(counter)

@app.route('/counter', methods=['GET'])
def get_counter():
    global counter
    return jsonify({'counter': counter})

@app.route('/counter/increment', methods=['POST'])
def increment_counter():
    global counter
    counter += 1
    return jsonify({'counter': counter})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)

