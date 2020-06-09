from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

METADATA = MetaData()
Base = declarative_base(metadata=METADATA)

DB = SQLAlchemy(metadata=METADATA)
