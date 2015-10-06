#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'H.M.Yang'

import MySQLdb

try:
    conn = MySQLdb.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'centos',
            db = 'test',
            port = 3306,
            )
    cur = conn.cursor()
#    insert_data = "INSERT INTO students(name, sex, degree) VALUES('Alex', 1, 90)"
    insert_data = "INSERT INTO students(name, sex, degree) VALUES(%s, %s, %s)"
    cur.execute(insert_data, ('Jack', 2, 78))
    cur.execute('select * from students')
    print('{}'.format(cur.fetchall()))
    # cur.fetchmany(num) 
    conn.rollback()
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error as err:
    print('MySQLdb error {0}'.format(err))
