from flask import Flask, jsonify, request
import qrcode
import qrCodeGenerator

app = Flask(__name__)


@app.route('/',methods=["POST"])
def gen():
    query = dict(request.form)['query']
    # query = "https://qr-code-genrator.herokuapp.com/generate"
    img = qrCodeGenerator.generate(query)
    res = "Image Created"
    json_file = {'query': res}
    return jsonify(json_file)


@app.route('/generate', methods=["POST"])
def generate_qr():
    query = dict(request.form)['query']
    # query = "https://qr-code-genrator.herokuapp.com/generate"
    img = qrCodeGenerator.generate(query)
    res = "Image Created"
    json_file = {'query': res}
    return jsonify(json_file)


if __name__ == '__main__':
    app.run(host="0.0.0.0")


def generate(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Add your link below in the quoted place
    qr.add_data(url)

    qr.make(fit=True)

    # Making an image of the generated qr code
    img = qr.make_image(fill_color="black", back_color="white")

    # Add the file name with which you want to save the QR code
    # img.save("file_name.png/jpg")
    return img
