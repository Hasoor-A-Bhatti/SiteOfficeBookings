import streamlit as st
from datetime import datetime

st.title("Check-Out")

# Initialize session_state dictionaries
if 'product_bookings' not in st.session_state:
    st.session_state.product_bookings = {}

if 'all_bookings' not in st.session_state:
    st.session_state.all_bookings = {}

# if 'all_transfers' not in st.session_state:
#     st.session_state.all_transfers = {}

# Display input boxes for Product ID and AIMS ID
with st.form(key="return_form", clear_on_submit=True):
    opcode= st.text_input("Operator Code", "", key="op")
    aims_id = st.text_input("AIMS ID", "")
    items_to_return = st.multiselect("Select Items to Remove", ["Drill", "Sander", "ScrewDriver", "Van"])
    submit_button = st.form_submit_button(label='Confirm')


if submit_button:
    if opcode == "99999":
        for product_id in items_to_return:
            if product_id in st.session_state.product_bookings:
                del st.session_state.product_bookings[product_id]


                for tool_name, tool_info in st.session_state.all_bookings.items():
                    for tool_data in tool_info:
                        if tool_data["AIMS"] == aims_id and tool_data["BOOKING STATUS"] == "ACTIVE" and tool_name == product_id:
                            tool_data["TIME RETURNED"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            tool_data["BOOKING STATUS"] = "RETURNED"

                st.success("Product checked out successfully!")
            else:
                st.warning("Product not found in bookings list.")
    else:
        st.warning("Invalid operator code!")

st.write("Current Product Bookings:", st.session_state.product_bookings)