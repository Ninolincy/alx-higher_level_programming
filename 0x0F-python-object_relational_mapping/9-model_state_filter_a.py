#!/usr/bin/python3
"""
script that lists all State objects that
contain the letter a from the database
"""


import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(
            State.name.contains('a')).order_by(State.id.asc()):
        print("{}: {}".format(state.id, state.name))

    session.close()
    