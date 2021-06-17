import os
from flask import Flask


def create_app(test_config=None):
    # Create and configure app
    app = Flask(import_name='app', instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
        SQLALCHEMY_DATABASE_URI=os.path.join(app.instance_path, 'app.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exits
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from app.models import db
    db.init_app(app)

    from app import user, auth, admin
    app.register_blueprint(user.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(admin.bp)

    return app
