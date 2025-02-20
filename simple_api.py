from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
    return jsonify(result="hello world")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
