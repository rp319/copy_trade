import datetime
import os

from alice_blue import *
import user_details
import user_detail2
import time
from datetime import datetime,time

username = user_details.username
password = user_details.password
twofa = user_details.twofa
api_secret = user_details.app_secret
appid = user_details.app_id
opentime = time(hour=9, minute=15, second=0)
closetime = time(hour=15, minute=30, second=0)
today = datetime.now().time()
while True:
    if today > opentime and  today < closetime :

            access_token = AliceBlue.login_and_get_access_token(username=username, password=password, twoFA=twofa,api_secret=api_secret, app_id=appid)

            if os.path.getsize('Access_token.txt')==0:
                file = open("Access_token.txt", "w")
                file.write(access_token)
            # while today > opentime and  today < closetime :
            else:
                file = open("Access_token.txt", "r")
                acctkn = file.readline()
                print(acctkn)
                alice = AliceBlue(username='username', password='password', access_token=acctkn)
                    # DATA Read
                print(alice.get_profile())  # get balance / margin limits


                # Code 17 Sept


                
                # print(alice.get_balance())
                # myorders = alice.get_order_history()
                # print(type(myorders))
                # l1 = myorders['data']['completed_orders']
                # print(l1[1])
                # break
                # print(alice.get_daywise_positions())



    else:
        file = open("Access_token.txt","r+")
        file.truncate(0)
        file = open("Access_token.txt","r")
        print(file.readline())
        file.close()
        print("Try Again Between 9:15AM to 3:30PM")
        break