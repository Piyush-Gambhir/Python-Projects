# Importing the qrcode module
import qrcode

# Define the data to be encoded in the QR code
qr_data = "Hello World!"

# Generate the QR code
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=5,
    border=1,
)
qr.add_data(qr_data)
qr.make(fit=True)

# Create an image from the QR code and save it
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")
