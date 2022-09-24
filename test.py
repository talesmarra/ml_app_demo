import requests
import json

url = "http://localhost:5000/predict"
data = {
"text": 'test'
}
# Convert to JSON string
input_data = json.dumps(data)
# Set the content type
headers = {"Content-Type": "application/json"}
# Make the request and display the response
resp = requests.post(url, input_data, headers=headers)
print(resp.text)