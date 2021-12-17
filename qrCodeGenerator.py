# A project to generate a QR code for an URL

import qrcode
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# # Add your link below in the quoted place
# qr.add_data('https://www.youtube.com/watch?v=Az9kvKlEbJU')
#
# qr.make(fit=True)
#
# # Making an image of the generated qr code
# img = qr.make_image(fill_color="black", back_color="white")
#
# #Add the file name with which you want to save the QR code
# img.save("file_name.png/jpg")


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
