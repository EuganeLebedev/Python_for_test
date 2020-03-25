import requests

r = requests.get("http://example.com")
print(r.status_code)
print(r.text)

