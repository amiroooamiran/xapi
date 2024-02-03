import requests

url = "http://localhost:5000/receive-data"
data = {
    "search_query": "hello",
    "filters": "iran"
}
headers = {"Content-Type": "application/json"}  # Set the Content-Type header
response = requests.post(url, json=data, headers=headers)
print(response.text)