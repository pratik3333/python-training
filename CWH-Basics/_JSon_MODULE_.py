import json

# data='{"var1":"pratik","var2":653}'
# #
# # parase=json.loads(data)
# # print(parase['var1'])
# print(json.load(data))

data2={
       "channel_name":"Codewithharry",
       "Mobiles":['Iphone','MI','Nokia','Samsung']
}

jscomp=json.dumps(data2)
print(jscomp)