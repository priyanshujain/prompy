import prometheus_client 
from flask import Flask, jsonify, Response
from helper import setup_request_metrics

app = Flask(__name__)
setup_request_metrics(app)

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

@app.route("/")
def generate_message():
    return jsonify({'message':"Welcome"})

@app.route("/api/v1")
def generate_response():
    0/0
    return jsonify({'message':"Welcome to test API"})


@app.route("/500")
def generate_500():
    0/0
    return jsonify({'message':"Internal server error"})

@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)