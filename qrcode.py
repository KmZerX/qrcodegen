import pyqrcode
import png

print("Welcome To KMQR Gen!")
link = input("Input Your URL :")
qr_code = pyqrcode.create(link)
qr_code.png("qrcreate.png", scale=5)