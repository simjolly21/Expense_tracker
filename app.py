import qrcode
from PIL import Image
# Data to encode
data = {
    "Name": "John Doe",
    "Date of Birth": "1985-06-15",
    "Address": "123 Maple St, Toronto, ON",
    "Identification Number": "123456789",
    "Card Expiry Date": "2028-12-31",
    "Issuing Authority": "Ontario Ministry of Transport",
    "Additional Security Info": "Hologram ID: 987654321"
}
# Create QR Code
qr = qrcode.QRCode(version=10, box_size=10, border=10)
qr.add_data(str(data))
qr.make(fit=True)
# Create image
img = qr.make_image(fill='black', back_color='white')
# Save the image
img.save("Canada_ID_QR_Code.png")