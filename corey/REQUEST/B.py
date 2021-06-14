import requests
payload={'username':'pratik','password':'abc'}
r=requests.post('https://httpbin.org/post', data=payload)

print(r.json())
print(r.text)

