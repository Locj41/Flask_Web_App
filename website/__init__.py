from flask import Flask
import secrets



def create_app():
    app = Flask(__name__)
    secret = secrets.token_urlsafe(32)
    app.secret_key = secret
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

