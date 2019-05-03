import requests

class Postcode:
    def __init__(self, postcode, status, result):
        self.postcode = postcode
        self.status = status
        self.result = result

        #you need to have a ststus and result

    def look_up_one_postcode(self, post_codes):
        post_codes = requests.get('https://api.postcodes.io/postcodes/E146HS')
        # not hardoce your post code
        #access the result of the query
            # save the status to the attributes of the objct
            # save the result to the attributes of the objct






















        print(post_codes)
        for key in post_codes.json()['result']:
            print('key:', key)
            print('value:', post_codes.json()['result'][key])

    look_up_one_postcode()
    print(look_up_one_postcode())


    def Print_region_country(self):
        pass

    def Print_all_details(self):
        pass

    def Latitude_long_Print(self):
        pass

        post_codes = requests.get('https://api.postcodes.io/postcodes/E146HS')
        print(post_codes)
        print(type(post_codes.json()))
        print(post_codes.json().keys())

        for key in post_codes.json()['result']:
            print('key:', key)
            print('value:', post_codes.json()['result'][key])


