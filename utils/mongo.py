import os
from mongoengine import connect


def get_connection_url() -> str:
    url = "mongodb+srv://abc:{}@cluster0.ensok.mongodb.net/abc-{}?retryWrites=true&w=majority".format(
        os.environ["PASS_NEW"], os.environ["STAGE"]
    )

    return url


def db_config():
    try:
        uri: str = get_connection_url()
        connect(host=uri)
    except KeyError:
        connect("mongoenginetest", host="mongomock://localhost")
