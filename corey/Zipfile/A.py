import requests

r=requests.get('https://www.ripleys.com/wp-content/uploads/2020/02/shutterstock_1348113467-1024x683.jpg')

with open('panther.png','wb') as f:
    f.write(r.content)
    f.close()