import json

player={
    "jerseyno":4,
    "name":"vigil van dijk",
    "gender":"male",
    "age":29,
    "country":"netherlands",
    "club":"liverpool",
    "position":"defender"
}
file=open("playerdetails.json","w")
json.dump(player,file)
print('data stored in JSON file...')
file.close()