import random
from time import sleep
import streamlit as st
from datetime import datetime

# Initialize session_state dictionaries
if 'product_bookings' not in st.session_state:
    st.session_state.product_bookings = {}

if 'all_bookings' not in st.session_state:
    st.session_state.all_bookings = {}

# if 'all_transfers' not in st.session_state:
#     st.session_state.all_transfers = {}

    # Display input boxes for Product ID and AIMS ID
# Get user input
with st.form(key="booking_form", clear_on_submit=True):
    opcode= st.text_input("Operator Code", "", key="op")
    aims_id = st.text_input("AIMS ID", "", key="aims")
    # Display basket items
    selected_items = st.multiselect("View <> Select Items to Remove", ["Drill", "Sander", "ScrewDriver", "Van"])
    submit_button = st.form_submit_button(label='Confirm')


# Confirm button
if submit_button:
    #empty input box
    # Save basket items to dictionary
    current_time = datetime.now()

    for item in selected_items:
        if opcode == "99999":
            if item not in st.session_state.product_bookings:
                st.session_state.product_bookings[item] = []
                st.session_state.product_bookings[item] = {
                "AIMS": aims_id,
                "TIME BORROWED": current_time.strftime("%Y-%m-%d %H:%M:%S")}

                if item not in st.session_state.all_bookings:
                    st.session_state.all_bookings[item] = []
                
                st.session_state.all_bookings[item].append({
                "AIMS": aims_id,
                "BOOKING STATUS": "ACTIVE",    
                "TIME BORROWED": current_time.strftime("%Y-%m-%d %H:%M:%S"),
                "AUTHORIZED BY": opcode})
                
                
                st.success("Product added to booking list!")
                
            else:
                st.warning("Product already booked!")
        else:
            st.warning("Invalid operator code!")

# Print the current product bookings
st.write("Current Product Bookings:", st.session_state.product_bookings)
st.write("Current All Bookings:", st.session_state.all_bookings)
