from flask import Blueprint, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
from datetime import datetime
from app.db import Data
import os

bp = Blueprint('pi', __name__, url_prefix='/pi')

auth = HTTPBasicAuth()
PI_USERNAME = os.environ['PI_USERNAME']
PI_PASSWORD = os.environ['PI_PASSWORD']
# This basic authentication scheme is created for routes exposed for the Pi to send data
# and is different from the one defined for admin user logins.
# This functionality was created to secure routes called by the
# pi without having to create an admin user for the pi which will
# need to be validated with a different login_required hook.

@auth.verify_password
def verify_pi(username, password):
    """Counter check against environment variables that the credentials are correct"""
    if username == PI_USERNAME and check_password_hash(PI_PASSWORD, password):
        return username


@bp.route('/data', methods=['POST'])
@auth.login_required
def receive_data():
    """Endpoint to receive data from Pi"""
    data = request.get_json()
    datetime_obj = datetime.fromisoformat(data['timestamp'])
    Data.add_data(datetime_obj,
                  data['img1'],
                  data['img2'],
                  data['img3'],
                  data['img4'],
                  data['img5'],
                  data['mode']) #TODO change this to 'highest' once Data class has been updated on the RPI
    return "Success"