__author__ = 'tbh3f'


import csv
import sqlite3

database = 'lab3.db'  # global variable to hold database name

def write_one_to_db_version1():
    """ demos writing one record to the DB, but doesn't use Python variables"""
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        sql_cmd = "insert into coursedata values('STS', 1500, 1122, 'Lecture', 20, 20, 'T. Jefferson')"
        cur.execute(sql_cmd)

def write_one_to_db_version2(dept, courseNum):
    """ demos writing one record to the DB, uses string concat (don't do this!)"""
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        # have to remember to use single-quotes in next line to handle text column in DB
        sql_cmd = "insert into coursedata values('" + dept + "', " + \
           str(courseNum) + ", 1122, 'Lecture', 20, 20, 'T. Jefferson')"
        cur.execute(sql_cmd)

def write_one_to_db_version3(dept, courseNum):
    """ demos writing one record to the DB, uses string format (better, but still ugly)"""
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        # have to remember to use single-quotes in next line to handle text column in DB
        sql_cmd = "insert into coursedata values('{0}', {1}, 1122, 'Lecture', 20, 20, 'T. Jefferson')"
        sql_cmd = sql_cmd.format(dept, courseNum)
        cur.execute(sql_cmd)

def write_one_to_db_version4(dept, courseNum):
    """ demos writing one record to the DB, uses parameter substitution (DO IT THIS WAY!)"""
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        sql_cmd = "insert into coursedata values(?, ?, 1122, 'Lecture', 20, 20, 'T. Jefferson')"
        cur.execute(sql_cmd, (dept, courseNum)) # use ? in command string and a tuple to fill in each ?
        # this is nice, clean, simple. Don't have to remember quotes.  Also, avoids security risk!

#This is an edit for the merge section of Lab6


# if __name__ == "__main__":

    # Here are some methods that demo how to write data to a DB with sqlite.
    # Uncomment out each of the calls below and see what it does.
    # The trick is creating the SQL command string.  The 4th version is THE RIGHT way to do this.

    # write_one_to_db_version1()
    # write_one_to_db_version2('APMA', 2120)
    # write_one_to_db_version3('ENGR', 1620)
    # write_one_to_db_version4("XXX's", 2150)

