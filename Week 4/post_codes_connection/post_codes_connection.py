import requests

class PostCodesConnection:

    def __init__(self):

        self.path = 'https://api.postcodes.io/postcodes/'
        self.parameters = ''
        self.status = 'No connection attempt yet'
        self.result = 'No connection attempt yet'

    def look_up_one_post_code(self, post_code):

        # I have to look up a post code
            # build our path / lkink / using the parameters
            # call / make the request
            # capture it in a variable

        url_path = self.path + post_code # -> https://api.postcodes.io/postcodes/B237Ql
        api_postcodes_call = requests.get(url_path)
        api_dict = api_postcodes_call.json()
        self.status = api_dict['status']
        self.result = api_dict['result']
        print(self.status)

        # update the result and status attribute

    def prin_region_country(self):
        # use self.result to get access to the data i need to print
        print('Country:', self.result['country'])
        print('Region:', self.result['region'])

    def print_lat_long(self):
        print('Lat:', self.result['latitude'])
        print('Long:', self.result['longitude'])

    def print_all_details(self):
        for key in self.result:
            print(key, '->', self.result[key])

    def print_access_one_value(self, key):
        print(self.result[key])
