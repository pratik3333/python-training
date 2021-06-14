import requests

r=requests.get('https://www.traveller.com.au/content/dam/images/g/z/b/x/u/r/image.related.articleLeadwide.620x349.gzbzf5.png/1509681035017.jpg')
with open('image.png','wb') as f:
    f.write(r.content)
