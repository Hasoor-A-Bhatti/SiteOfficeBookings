import streamlit as st
from datetime import datetime

# Initialize product bookings dictionary in session state
# Initialize session_state dictionaries
if 'product_bookings' not in st.session_state:
    st.session_state.product_bookings = {}

if 'all_bookings' not in st.session_state:
    st.session_state.all_bookings = {}

# if 'all_transfers' not in st.session_state:
#     st.session_state.all_transfers = {}

# Page layout
st.title("SITE OFFICE BOOKING PORTAL")
# Print the current product bookings
st.write("Current Product Bookings:", st.session_state.product_bookings)
