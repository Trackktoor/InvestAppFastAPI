from datetime import datetime
from sqlalchemy import JSON, MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column


metadata = MetaData()

roles = Table(
    'roles',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("premissions", JSON),
)

users = Table(
    'users',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registrated_at", TIMESTAMP, default=datetime.utcnow()),
    Column("role_id", Integer, ForeignKey('roles.id')),
)