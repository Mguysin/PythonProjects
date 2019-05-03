import requests

import json

# create a json to send
# fill in the headers
# make our request

json_body = json.dumps({"postcodes": ['E166HS', 'RM141SW', 'E148LH']})

headers = {'Content-Type': 'application/json'}

post_requests_to_postcodes = requests.post('https://api.postcodes.io/postcodes', headers=headers, data=json_body)

print(post_requests_to_postcodes.json())

