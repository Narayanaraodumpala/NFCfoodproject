import random
import qrcode
x=random.randint(1000,99999)

qr=qrcode.make('your otp is'+str(x))
qr.show()

