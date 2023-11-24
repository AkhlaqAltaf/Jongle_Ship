from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from PIL import Image

# Create a PDF buffer
pdf_buffer = BytesIO()

# Create a PDF canvas
c = canvas.Canvas(pdf_buffer, pagesize=letter)

# Load the base64 encoded label image
base64_image = your_label_data['customerLogos'][0]['content']
image_data = base64_image.decode('base64')  # Assuming Python 2, use base64.b64decode() for Python 3

# Create an Image instance from the image data
img = Image.open(BytesIO(image_data))

# Set the image size
img_width, img_height = img.size

# Draw the image on the PDF canvas
c.drawImage(img, 100, 500, width=img_width, height=img_height)

# Add additional text or annotations if needed
c.setFont("Helvetica", 12)
c.drawString(100, 450, "Additional Information: Your text here")

# Save the PDF canvas
c.save()

# Save the PDF buffer to a file
pdf_filename = "shipment_label.pdf"
with open(pdf_filename, 'wb') as pdf_file:
    pdf_file.write(pdf_buffer.getvalue())

# Close the PDF buffer
pdf_buffer.close()

print(f"PDF saved as {pdf_filename}")
