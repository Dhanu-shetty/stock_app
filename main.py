#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 00:53:18 2021

@author: dhanu
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 00:53:18 2021

@author: dhanu
"""
from nsetools import Nse
nse = Nse()
import threading
import sched, time
s = sched.scheduler(time.time, time.sleep)

import sqlite3
from stock_db_api import stock_db_api


a =stock_db_api()
user = stock_db_api.get_All_user_data(a)
#print(user)


def check_condition(value,condition):
        if(condition[0 : 1] == '>'):
            if value > int(condition[1 : ]):
                return 1
            else :
                return 0
        if(condition[0 : 1] == '<'):
            if value < int(condition[1 : ]):
                return 1
            else :
                return 0
        if(condition[0 : 1] == '='):
            if value == int(condition[1 : ]):
                return 1
            else :
                return 0
    

def process_data():
    begin = time.time()
    for tupul in user:
        orders_by_id = stock_db_api.get_order_by_ID(a,tupul[0])
        for tupul1 in orders_by_id:
            value = nse.get_quote(tupul1[2])["lastPrice"]
            if (check_condition(value,tupul1[3]))== 1:
                print("condition true notification to user")
            else:
                print("no notification needed")
    end = time.time()

    print("Total time taken in : process_data ->", end - begin)




def Prosess_order_based_on_user(orders_by_id):
    for tupul1 in orders_by_id:
        value = nse.get_quote(tupul1[2])["lastPrice"]
        if (check_condition(value,tupul1[3]))== 1:
            print("condition true notification to user")
        else:
            print("no notification needed")



thread_list =[]
def process_data_thread():
    begin = time.time()
    for tupul in user:
        orders_by_id = stock_db_api.get_order_by_ID(a,tupul[0])
        t1 = threading.Thread(target=Prosess_order_based_on_user, args=(orders_by_id,))
        t1.start()
        thread_list.append(t1)
        
    while True:  
        for i in thread_list:
            i.join()  
        break
    end = time.time()
    print("Total time taken in : process_data_thread ->", end - begin)

if __name__ == "__main__":
    data = "My data read from the Web"
    process_data()
    process_data_thread()

