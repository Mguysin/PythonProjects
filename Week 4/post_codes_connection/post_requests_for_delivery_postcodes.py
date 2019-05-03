import requests

import json



# create a json to send
# make our request

json_body = json.dumps({"postcodes": ['E146HS', 'RM141SW', 'E148LH']})

headers = {'Content-Type': 'application/json'}

print(json_body)

post_resquet_to_postcodes = requests.post('https://api.postcodes.io/postcodes', headers=headers, data=json_body)

print(post_resquet_to_postcodes.json())





