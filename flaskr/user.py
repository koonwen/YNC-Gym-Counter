from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flaskr.db import get_db

bp = Blueprint('user', __name__)


@bp.route('/')
def index():
    db = get_db()
    latest = db.execute('SELECT timestamp, average FROM data LIMIT 1;').fetchone()
    if latest is None:
        average = "ERROR"
        timestamp = "ERROR"
    else:
        average = latest['average']
        timestamp = latest['time']
    return render_template('index.html', number=average, timestamp=timestamp)