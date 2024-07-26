import qrcode as qr
# make Qr code
img = qr.make("https://www.linkedin.com/in/arthana-kk-9a078b191/")
# save qr code as image
img.save("Arthana.png")