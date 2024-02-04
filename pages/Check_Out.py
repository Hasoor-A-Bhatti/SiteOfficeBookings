import streamlit as st
from datetime import datetime

st.title("Check-Out")

# Initialize session_state dictionaries
if 'product_bookings' not in st.session_state:
    st.session_state.product_bookings = {}

if 'all_bookings' not in st.session_state:
    st.session_state.all_bookings = {}

if 'all_transfers' not in st.session_state:
    st.session_state.all_transfers = {}

    # Display input boxes for Product ID and AIMS ID
product_id = st.text_input("Product ID", "")
aims_id = st.text_input("AIMS ID", "")

if st.button("Confirm"):
    if product_id in st.session_state.product_bookings:
        del st.session_state.product_bookings[product_id]
        st.session_state.all_bookings[product_id]["TIME RETURNED"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.success("Product checked out successfully!")
    else:
        st.warning("Product ID not found in booking list.")

st.write("Current Product Bookings:", st.session_state.product_bookings)