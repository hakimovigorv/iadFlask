import psycopg2
import sqlalchemy as db
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean
from sqlalchemy.ext.declarative import as_declarative, declarative_base

engine = db.create_engine("postgresql+psycopg2://postgres:123@localhost/iad2")
engine.connect()

Base = declarative_base()

blog = Table('blog', metadata,
    Column('id', Integer(), primary_key=True),
    Column('post_title', String(200), nullable=False),
    Column('post_slug', String(200),  nullable=False),
    Column('content', Text(), nullable=False),
    Column('published', Boolean(), default=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)


