import streamlit as st
import requests

st.title("H8- FTDS 10 Milestone 2 - Hussein Muhammad")
st.subheader("Aplikasi Fraud Detection")
st.write('')
distance_from_home = st.number_input("Distance From Home During the Transaction")
distance_from_last_transaction = st.number_input("Distance from the last Transaction")
ratio_to_median_purchase_price = st.number_input("Ratio to the Median Purchase Price")
repeat_retailer = st.selectbox("On Repeated Retailer?", [0, 1])
used_chip = st.selectbox("Age", [0, 1])
used_pin_number = st.selectbox("Parent / Children", [0, 1])
online_order = st.selectbox("Gender", [0, 1])

# inference
data = {'distance_from_home':distance_from_home,
        'distance_from_last_transaction':distance_from_last_transaction,
        'ratio_to_median_purchase_price': ratio_to_median_purchase_price,
        'repeat_retailer':repeat_retailer,
        'used_chip':used_chip,
        'used_pin_number':used_pin_number,
        'online_order':online_order}

URL = ""

# komunikasi
r = requests.post(URL, json=data)
res = r.json()
if res['code'] == 200:
    st.title(res['result']['classes'])

  