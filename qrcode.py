import pyqrcode
import png

# Get user inputs
name = input("Enter your name: ")
fellow_id = input("Enter your fellow ID: ")

# Define the function to generate the QR code
def generate_qr_code():
    data = f"{name}|{fellow_id}"
    url = pyqrcode.create(data)
    url.png("Your_ID.png", scale=5)

# Call the function with user inputs
generate_qr_code()
