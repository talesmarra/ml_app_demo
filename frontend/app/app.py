import requests
import json
import streamlit as st

url = "http://backend.docker:5000/predict"

st.title("The review classifier")
st.markdown("The app that classifies your reviews!")
text = st.text_input("Type your review")
data = {
    "text": text
}
if text:
    # Convert to JSON string
    input_data = json.dumps(data)
    # Set the content type
    headers = {"Content-Type": "application/json"}
    # Make the request and display the response
    resp = requests.post(url, input_data, headers=headers)
    st.write(resp.text)
