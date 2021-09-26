#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 00:53:18 2021

@author: dhanu
"""

import sched, time
s = sched.scheduler(time.time, time.sleep)

import sqlite3


class User:
    """A sample Employee class"""

    def __init__(self, ID, Name, Number ,Email):
        self.ID = ID
        self.Name = Name
        self.Number = Number
        self.Email = Email

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

c =conn.cursor()


# =============================================================================
# c.execute("""CREATE TABLE user (
#              ID integer,
#              Name text,
#              Number integer,
#              Email text
#              )""")
# 
# =============================================================================



def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO user VALUES (:ID, :Name, :Number, :Email)", {'ID': emp.ID, 'Name': emp.Name, 'Number': emp.Number ,'Email': emp.Email})

def get_emps_by_name(Name):
    c.execute("SELECT * FROM user WHERE Name=:Name", {'Name': Name})
    return c.fetchall()

def get_emps_by_All():
    c.execute("SELECT * FROM user")
    return c.fetchall()

def update_Number(user, Number):
     with conn:
         c.execute("""UPDATE user SET Number = :Number
                     WHERE Name = :Name """,
                   {'Name': user.Name, 'Number': Number})
 
 
def remove_user(user):
     with conn:
         c.execute("DELETE from user WHERE Name = :Name ",
                   {'Name': user.Name})
 


User_1 = User(1, 'dhanu', 9844866741 ,'dhananjay.shetty50@gmail.com')
User_2 = User(2, 'vajja', 9844866742 ,'dhananjay.shetty50@gmail.com' )

insert_emp(User_1)
insert_emp(User_2)

#remove_user(User_2)
emps = get_emps_by_All()
print(emps)

conn.commit()

conn.close()

