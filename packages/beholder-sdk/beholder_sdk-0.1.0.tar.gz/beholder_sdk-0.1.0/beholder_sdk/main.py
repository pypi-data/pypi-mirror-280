from flask import Flask
from fastapi import FastAPI
from beholder_sdk.middleware import django_middleware, flask_middleware, fastapi_middleware


def beholder(app, db_engine=None):
    if isinstance(app, str):
        if app == "django":
            return django_middleware.DjangoCollectorMiddleware("django", db_engine)
    elif hasattr(app, 'wsgi_app') and 'flask' in str(type(app)):
        return flask_middleware.FlaskCollectorMiddleware(app, db_engine)
    elif hasattr(app, 'add_middleware') and 'fastapi' in str(type(app)):
        return fastapi_middleware.FastApiCollectorMiddleware(app, db_engine)
    return None
