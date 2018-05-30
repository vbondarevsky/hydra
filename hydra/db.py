from sqlalchemy import (
    MetaData, Table, Column, Integer, String
)


meta = MetaData()

node = Table(
    "node", meta,

    Column("id", Integer, primary_key=True),
    Column("name", String(150), nullable=False),
    Column("url", String(256), nullable=False),
    Column("user", String(100), nullable=False),
    Column("password", String(100), nullable=False),
)
