from flask import Flask, jsonify, request
import datetime
import socket

app = Flask(__name__)


@app.route('/api/v1/details', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):


        return jsonify({
            'time': datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"),
            'hostname': socket.gethostname(),
            'message': 'teste de versao python gitHub action pipeline v3.3'
            })


@app.route('/api/v1/healthz', methods = ['GET', 'POST'])
def health():
    if(request.method == 'GET'):

        return jsonify({
            'status': 'up'


            }), 200

@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):

    return jsonify({'data': num**2})


# driver function
if __name__ == '__main__':

    app.run(host="0.0.0.0")