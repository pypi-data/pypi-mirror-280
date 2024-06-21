from pytest import fixture
from dotenv import load_dotenv
import os

load_dotenv()


@fixture
def igdb_secrets():
    return os.getenv("IGDB_ID"), os.getenv("IGDB_SECRET")
