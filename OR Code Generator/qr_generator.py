import qrcode

qr = input("Enter URL: ").strip()

qrc = qrcode.make(qr)
qrc.save("QRCODE.png")
