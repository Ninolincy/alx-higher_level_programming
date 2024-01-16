#!/usr/bin/python3
"""A script that takes in arguments and displays all values in the states."""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1],
                               passwd=argv[2],
                               db=argv[3])

    try:
        curs = database.cursor()
        curs.execute("SELECT * FROM states WHERE name\
                    LIKE %s ORDER BY states.id\
                    ASC", [argv[4]])
        rows = curs.fetchall()
        for row in rows:
            print(row)
        curs.close()
    except MySQLdb.Error as e:
        print(f"Error executing the query: {e}")
    database.close()