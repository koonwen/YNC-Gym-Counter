from flask import Blueprint, render_template
from app.views.auth import login_required
from app.db import Data, Admin

bp = Blueprint('admin', __name__, url_prefix='/admin')

# TODO Fix display
# TODO Select number of rows & see if you can simply query
@bp.route('/')
@login_required
def index():
    """Admin index page showing data table"""
    latest_n_entries = Data.get_latest_n_entries()
    admin_usernames = Admin.get_all_admin_usernames()
    return render_template('admin.html',
                           entries=latest_n_entries,
                           admin_usernames=admin_usernames)
