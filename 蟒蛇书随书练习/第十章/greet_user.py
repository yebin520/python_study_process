import json
filename = 'file_work/username.json'
with open(filename) as f:
    name = json.load(f)
    print (name)