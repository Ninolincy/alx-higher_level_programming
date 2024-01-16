#!/usr/bin/python3
"""
A script that takes in the name of a
state as an argument and lists all cities of that state.
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    database = MySQLdb.connect(user=argv[1],
                               passwd=argv[2],
                               db=argv[3])
    try:
        curs = database.cursor()
        curs.execute("SELECT cities.name FROM cities INNER JOIN states ON \
                    cities.state_id=states.id WHERE states.name LIKE %s \
                    ORDER BY cities.id ASC", [argv[4]])
        rows = curs.fetchall()
        s = []
        print(", ".join(row[0] for row in rows))
        curs.close()
    except MySQLdb.Error as e:
        print(f"Error executing the query: {e}")
    database.close()