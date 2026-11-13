import requests

url = "http://127.0.0.1:5000/api/chat"
data = {"message": "سلام، این پیام تست منه"}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())