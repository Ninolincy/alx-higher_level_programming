#!/usr/bin/python3
"""Search for states by name in MySQL database."""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1],
                               passwd=argv[2],
                               db=argv[3])
    try:
        curs = database.cursor()
        curs.execute("SELECT * FROM states WHERE\
                    name LIKE BINARY '{}'\
                    ORDER BY states.id ASC".format(argv[4]))
        rows = curs.fetchall()
        for row in rows:
            print(row)
        curs.close()
    except MySQLdb.Error as e:
        print(f"Error executing the query: {e}")
    database.close()