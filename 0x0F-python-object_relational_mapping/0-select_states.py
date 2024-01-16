#!/usr/bin/python3
"""List all states available from a MySQL database."""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    database = MySQLdb.connect(port=3306,
                               host='localhost',
                               charset='utf8',
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])
    try:
        curs = database.cursor()
        curs.execute("SELECT * FROM states ORDER BY id ASC")
        rows = curs.fetchall()
        for row in rows:
            print(row)
        curs.close()
    except MySQLdb.Error as e:
        print(f"Error fetching data from the database: {e}")
    database.close()