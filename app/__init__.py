import os
from dotenv import load_dotenv
from flask import Flask


def create_app(test_config=None):
    # Create and configure app
    app = Flask(import_name='app', instance_relative_config=True)
    app.config['SECRET_KEY']='dev',
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///../instance/site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    # app.permanent_session_lifetime = False

    if test_config is None:
        # load the instance config, if it exists, when not testing
        load_dotenv(verbose=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exits
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Extensions
    from app.db import db, add_db_utils
    db.init_app(app)
    add_db_utils(app)

    # Blueprints
    from app.views import user, auth, admin, pi
    app.register_blueprint(user.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(pi.bp)

    return app
