#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 10:36:23 2021

@author: dhanu
"""
import sqlite3
#conn = sqlite3.connect('stock.db')

#d =conn.cursor()



class stock_db_api:
        # Initializing
    conn =sqlite3.connect('stock.db')
    d=conn.cursor()
    #print('db session opend.')
    def __init__(self):
        conn = sqlite3.connect('stock.db')
        d =conn.cursor()
        print('db session opend.')
  
    # Deleting (Calling destructor)
    def __del__(self):
        print('db session closed')
        self.conn.commit()
        self.conn.close()
    def get_All_user_data(self):
        self.d.execute("SELECT * FROM user")
        return self.d.fetchall()
    def get_order_by_ID(self,ID):
        self.d.execute("SELECT * FROM users_order WHERE ID=:ID", {'ID': ID})
        return self.d.fetchall()
    def get_All_order(self):
        self.d.execute("SELECT * FROM users_order")
        return self.d.fetchall()


    