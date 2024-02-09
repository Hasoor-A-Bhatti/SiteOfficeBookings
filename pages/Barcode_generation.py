import streamlit as st
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw
import io

def generate_barcode(input_data):
    # Generate barcode
    barcode = Code128(input_data, writer=ImageWriter())

    # Create a BytesIO object to hold the image data
    img_bytes = io.BytesIO()

    # Save the barcode image to the BytesIO object
    barcode.write(img_bytes)
    img_bytes.seek(0)

    # Open the image using PIL
    img = Image.open(img_bytes)
    return img

# Streamlit UI
st.title('Barcode Generator')
input_data = st.text_input('Enter data for barcode generation:')
if st.button('Generate Barcode'):
    if input_data:
        barcode_image = generate_barcode(input_data)
        st.image(barcode_image, caption=f'Barcode for {input_data}', use_column_width=True)
    else:
        st.warning('Please enter some data to generate a barcode.')
