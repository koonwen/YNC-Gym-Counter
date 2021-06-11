from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/')
@login_required
def index():
    db = get_db()
    latest = db.execute('SELECT * FROM data LIMIT 1;').fetchone()
    average = latest['average']
    return render_template('index.html', number=average)
