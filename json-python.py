import json,urllib.request
url="https://jsonplaceholder.typicode.com/users"

jsonData=urllib.request.urlopen(url)

response=jsonData.read()
covert_str=str(response)

rp=covert_str.replace("\\n","\n").replace("b'","").replace("]'","]")

json_load=json.loads(rp)

for item in json_load:
    print(item["name"])
