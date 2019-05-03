import requests

class Postcode:
    def __init__(self, postcode):
        self.postcode = postcode

    def look_up_one_postcode(self,pcode):
        post_codes = requests.get('https://api.postcodes.io/postcodes/E146HS')

    def Print_region_country(self):
        print(post_codes)

    def Print_all_details(self):
        for key in post_codes.json()['result']:
            print('key:', key)
            print('value:', post_codes.json()['result'][key])

    def Latitude_long_Print(self):
        pass

        post_codes = requests.get('https://api.postcodes.io/postcodes/E146HS')

        print(post_codes)
        print(type(post_codes.json()))
        print(post_codes.json().keys())

        for key in post_codes.json()['result']:
            print('key:', key)
            print('value:', post_codes.json()['result'][key])
