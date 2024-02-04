import streamlit as st
from datetime import datetime

st.title("Oprator Functions")
# Initialize session_state dictionaries
if 'product_bookings' not in st.session_state:
    st.session_state.product_bookings = {}

if 'all_bookings' not in st.session_state:
    st.session_state.all_bookings = {}

if 'all_transfers' not in st.session_state:
    st.session_state.all_transfers = {}

st.write("OUTSTANDING Product Bookings:", st.session_state.product_bookings)

st.write("ALL Product Bookings:", st.session_state.all_bookings)

st.write("ALL Transfers:", st.session_state.all_transfers)

