from flask import Flask, jsonify, request
from QRCodeGenerator import qrCodeGenerator

app = Flask(__name__)


@app.route('/generate',methods=["POST"])
def generate_qr():
    query = dict(request.form)['query']
    img = qrCodeGenerator.generate(query)
    res = "Image Created"
    json_file = {'query': res}
    return jsonify(json_file)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
