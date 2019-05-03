import requests

post_codes = requests.get('https://api.postcodes.io/postcodes/E146HS')


print(post_codes)
print(type(post_codes.json()))
print(post_codes.json().keys())

for key in post_codes.json()['result']:
    print('key:', key)
    print('value:', post_codes.json()['result'][key])


# print(post_codes.status_code)
# print(post_codes.headers)
# print(post_codes.content)
# print(type(post_codes.json()))
# print(post_codes.json().keys())
# print(type(post_codes.json()['result']))
# print(post_codes.json()['result'])






print(post_codes.json())



# print(post_codes.json().keys())
# print(post_codes.json()['result'].keys())
#
#
# print(post_codes.json()['result']['parliamentary_constituency'])
# print(post_codes.json()['result']['country'])
# print(post_codes.json()['result']['admin_district'])
#
# for key in post_codes.json()['result']:
#     print(key, ':', post_codes.json()['result'][key])
#

