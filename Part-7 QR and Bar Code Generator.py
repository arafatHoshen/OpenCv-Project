import qrcode
from barcode import EAN13
QR = qrcode.make("Hello Bangladesh. Subscribe Nongare Hub")
QR.save("QR code1.png")

qrForFb =qrcode.QRCode(
    version=1,
    box_size=10,
    border=10
)
link = "https://www.youtube.com/channel/UCV6vGLwmJneo7leWpgjVBDA"
qrForFb.add_data(link)
qrForFb.make(fit=True)

img = qrForFb.make_image(fill="black", back_color="white")
img.save("Nongare Hub YouTube.png")

number = "1234567892222"
MyBarCode = EAN13(number)
MyBarCode.save("Barcode")