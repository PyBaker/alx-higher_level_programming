#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    """main function that lists all states from the database"""
    u_name = argv[1]
    p = argv[2]
    db_name = argv[3]
    st_n_s = argv[4]
    h = 'localhost'
    db = MySQLdb.connect(user=u_name, passwd=p, db=db_name, port=3306, host=h)
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name= %s"
    numrows = cur.execute(sql, (st_n_s, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
