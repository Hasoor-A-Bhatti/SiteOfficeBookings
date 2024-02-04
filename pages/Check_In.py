import streamlit as st
from datetime import datetime

st.title("Check-in")
# Initialize session_state dictionaries
if 'product_bookings' not in st.session_state:
    st.session_state.product_bookings = {}

if 'all_bookings' not in st.session_state:
    st.session_state.all_bookings = {}

if 'all_transfers' not in st.session_state:
    st.session_state.all_transfers = {}

product_id = st.text_input("Product ID", "", key="product_id")
aims_id = st.text_input("AIMS ID", "")

# Confirm button
if st.button("Confirm"):
    # Save product booking to dictionary
    st.session_state.product_bookings[product_id] = {
        "AIMS": aims_id,
        "TIME BORROWED": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    st.session_state.all_bookings[product_id] = {
        "AIMS": aims_id,
        "TIME BORROWED": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    st.success("Product booked successfully!")

st.write("Current Product Bookings:", st.session_state.product_bookings)