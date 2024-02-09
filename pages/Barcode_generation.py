import streamlit as st
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw
import io

def generate_barcode(input_data):
    # Generate barcode
    barcode = Code128(input_data, writer=ImageWriter())
    img_bytes = io.BytesIO()
    barcode.write(img_bytes)
    img_bytes.seek(0)
    # Open the image using PIL
    img = Image.open(img_bytes)
    return img

# Streamlit UI
st.title('Barcode Generator')
input_data = st.text_input('Enter Product Name')
if st.button('Generate Barcode'):
    if input_data:
        barcode_image = generate_barcode(input_data)
    else:
        st.warning('No product name entered.')
