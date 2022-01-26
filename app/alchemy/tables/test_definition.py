import sqlalchemy as sa
from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, LargeBinary, Numeric, String, Table, Text, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base
import json

import sys
import os
sys.path.append(os.getcwd() + '/..')

from alchemy.common.base import db

Base = declarative_base()
metadata = Base.metadata

import json
from sqlalchemy import MetaData, Table, Column, Integer, String, Date, Boolean,Text
from sqlalchemy.ext.declarative import declarative_base

import sys
import os
sys.path.append(os.getcwd() + '/..')

from alchemy.common.base import db

class TestDefinition(db.Model):
    __tablename__ = 'test_definitions'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)
