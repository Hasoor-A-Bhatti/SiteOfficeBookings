import streamlit as st
from datetime import datetime

st.title("Transfer")
# Initialize session_state dictionaries
if 'product_bookings' not in st.session_state:
    st.session_state.product_bookings = {}

if 'all_bookings' not in st.session_state:
    st.session_state.all_bookings = {}

# if 'all_transfers' not in st.session_state:
#     st.session_state.all_transfers = {}


with st.form(key="transfer_form", clear_on_submit=True):
    
    operator_code= st.text_input("Operator Code", "")
    old_aims_id = st.text_input("From AIMS", "")
    new_aims_id = st.text_input("Transferring to AIMS", "")
    items_to_return = st.multiselect("Select Items to Transfer", ["Drill", "Sander", "ScrewDriver", "Van"])
    submit_button = st.form_submit_button(label='Confirm')

if submit_button:
    for product_id in items_to_return:
        if product_id in st.session_state.product_bookings:
            
            st.session_state.product_bookings[product_id]["AIMS"] = new_aims_id
            st.session_state.product_bookings[product_id]["TRANSFERRED FROM"] = old_aims_id


            for tool_name, tool_info in st.session_state.all_bookings.items():
                    for tool_data in tool_info:
                        if tool_data["AIMS"] == old_aims_id and tool_data["BOOKING STATUS"] == "ACTIVE" and tool_name == product_id:
                            tool_data["AIMS"] = new_aims_id
                            tool_data["TRANSFERRED FROM"] = old_aims_id 
                            tool_data["TIME TRANSFERRED"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            tool_data["BOOKING STATUS"] = "ACTIVE - TRANSFERRED"
                            tool_data["TRANSFER AUTHORIZED BY"] = operator_code


            #NOT REQUIRED RIGHT NOW
            # st.session_state.all_transfers[product_id] = {
            # "FROM AIMS": st.session_state.product_bookings[product_id]["AIMS"],
            # "TO AIMS": new_aims_id,
            # "TIME TRANSFERRED": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            # "AUTHORIZED BY": operator_code
            # }

            st.success("Product transferred successfully!")
        else:
            st.warning("Invalid Product ID or Operator Code.")

