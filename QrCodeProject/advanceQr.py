import qrcode
from PIL import Image
import qrcode.constants

# create a QR code object
qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10, border = 5)
# add the data to the QR code object
qr.add_data("https://www.linkedin.com/in/arthana-kk-9a078b191/")
# Make Qr code
qr.make(fit=True)
# create an image from QR code
img = qr.make_image(fill_color = "blue", back_color = "white")
# Save the QR code image
img.save("Arthu.png")