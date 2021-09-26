#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 03:16:31 2021

@author: dhanu
"""
import sqlite3

class order:
    """A sample Employee class"""

    def __init__(self, ID, OrderID, Stock_name ,Condition):
        self.ID = ID
        self.OrderID = OrderID
        self.Stock_name = Stock_name
        self.Condition = Condition

# =============================================================================
#     @property
#     def email(self):
#         return '{}.{}@email.com'.format(self.first, self.last)
# 
#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
# 
#     def __repr__(self):
#         return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
# =============================================================================




conn = sqlite3.connect('stock.db')

d =conn.cursor()



# =============================================================================
# d.execute("""CREATE TABLE users_order (
#              ID integer,
#              OrderID integer,
#              Stock_name text,
#              Condition text
#              )""")
# =============================================================================



def insert_order(order):
    with conn:
        d.execute("INSERT INTO users_order VALUES (:ID, :OrderID, :Stock_name, :Condition)", {'ID': order.ID, 'OrderID': order.OrderID, 'Stock_name': order.Stock_name ,'Condition': order.Condition})

def get_order_by_ID(ID):
    d.execute("SELECT * FROM users_order WHERE ID=:ID", {'ID': ID})
    return d.fetchall()

def get_Order_by_All():
    d.execute("SELECT * FROM users_order")
    return d.fetchall()

def update_order_condition(order, Condition):
     with conn:
         d.execute("""UPDATE users_order SET Condition = :Condition
                     WHERE ID = :ID """,
                   {'ID': order.ID, 'Condition': Condition})
 
 
def remove_Order(OrderID):
     with conn:
         d.execute("DELETE from order WHERE OrderID = :OrderID ",
                   {'OrderID': OrderID})
 


User_1 = order(1, 1, "infy" ,'>1800')
User_2 = order(2, 1, "infy" ,'>1700' )

insert_order(User_1)
insert_order(User_2)

#remove_user(User_2)
emps = get_Order_by_All()
print(emps)


conn.commit()

conn.close()
