import streamlit as st
from datetime import datetime

st.title("Transfer")
# Initialize session_state dictionaries
if 'product_bookings' not in st.session_state:
    st.session_state.product_bookings = {}

if 'all_bookings' not in st.session_state:
    st.session_state.all_bookings = {}

if 'all_transfers' not in st.session_state:
    st.session_state.all_transfers = {}


product_id = st.text_input("Product ID", "")
new_aims_id = st.text_input("Transferring to AIMS", "")
operator_code= st.text_input("Operator Code", "")

if st.button("Confirm"):
    if product_id in st.session_state.product_bookings and operator_code == "99999":
        
        st.session_state.all_transfers[product_id] = {
        "FROM AIMS": st.session_state.product_bookings[product_id]["AIMS"],
        "TO AIMS": new_aims_id,
        "TIME TRANSFERRED": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "AUTHORIZED BY": operator_code
        }

        st.session_state.product_bookings[product_id]["AIMS"] = new_aims_id
        st.session_state.all_bookings[product_id]["AIMS"] = new_aims_id
        st.success("Product transferred successfully!")
    else:
        st.warning("Invalid Product ID or Operator Code.")

