from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from hydra.db.models import Base
from hydra.settings import settings


async def open_db(app):
    uri = f"sqlite:///{settings['db']['name']}.sqlite"
    engine = create_engine(uri)
    Base.metadata.create_all(engine)
    app["db"] = scoped_session(sessionmaker(bind=engine))


async def close_db(app):
    app["db"].remove()
