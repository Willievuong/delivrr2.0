from flask_sqlalchemy import Model, SQLAlchemy
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declared_attr, has_inherited_table
from sqlalchemy.dialects.postgresql import JSON

db = SQLAlchemy()
