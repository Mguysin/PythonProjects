from post_codes_connection import PostCodesConnection
postcodes_cont_instance = PostCodesConnection()

# print(postcodes_cont_instance.status)

# print(postcodes_cont_instance.result)
postcodes_cont_instance.look_up_one_post_code('B237Ql')

# print(postcodes_cont_instance.status)

# print(postcodes_cont_instance.result)
# postcodes_cont_instance.prin_region_country()
#
# postcodes_cont_instance.print_lat_long()
# postcodes_cont_instance.print_all_details()
postcodes_cont_instance.print_access_one_value('primary_care_trust')

