import datetime

from alice_blue import *
import  user_details
import time
import os
from datetime import datetime

username = user_details.username
password = user_details.password
twofa = user_details.twofa
api_secret = user_details.app_secret
appid = user_details.app_id
opentimehrs = 9
opentimemin = 14
closetimehrs = 15
closetimemin = 29
today = datetime.now()
currenthour = today.hour
currentminute = today.minute
# print(today.hour , today.minute)

access_token = AliceBlue.login_and_get_access_token(username=username, password=password, twoFA=twofa,
                                                        api_secret=api_secret, app_id=appid)

file = open("Access_token.txt", "w")
file.write(access_token)
file = open("Access_token.txt", "r")
acctkn = file.readline()
print(acctkn)
alice = AliceBlue(username='username', password='password', access_token=acctkn)

        # DATA Read

# print(alice.get_balance())  # get balance / margin limits
# print(alice.get_daywise_positions())
myprofile = alice.get_profile()

print("PAN Number : ",myprofile['data']['pan_number'],"\nName : ",myprofile['data']['name'])                #Nested Dictionary
# print(alice.get_profile())
# print(alice.get_profile)

# curr_time = today.strftime("%H:%M:%S")
# print(curr_time)
# print(time.localtime(tm_hour(),tm_min(),tm_sec()))