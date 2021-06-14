import requests


#r=requests.get('https://httpbin.org/basic-auth/pratik/testing', auth=('pratik','testing'))
#print(r) #<Response[200]> = success



r=requests.get('https://httpbin.org/basic-auth/pratik/testing', auth=('pratikms','testing'))
print(r) #<Response[401]> = unauthorised code