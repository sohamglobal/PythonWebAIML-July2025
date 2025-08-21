import json

file=open("playerdetails.json","r")
data=json.load(file)
print(data)
file.close()