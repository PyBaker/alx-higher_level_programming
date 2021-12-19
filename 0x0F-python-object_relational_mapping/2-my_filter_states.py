#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
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
    numrows = cur.execute("SELECT * FROM states WHERE \
     name LIKE BINARY '{}' ORDER BY id ASC".format(st_n_s))
    rows = cur.fetchall()
    for row in rows:
        print(row)
