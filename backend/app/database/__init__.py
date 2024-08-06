"""
Database module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from env import Postgres


Base = declarative_base()

postgres = Postgres()

connection_string = f'postgresql://{postgres.user}:{postgres.password}@{postgres.host}/{postgres.db}'

print(f"Connecting to\n{connection_string}")

engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)