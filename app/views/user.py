from flask import Blueprint, render_template
from app.db.models import Data
bp = Blueprint('user', __name__)

@bp.route('/')
def index():
    latest = Data.get_latest_entry()
    if not latest:
        average="No data yet"
        timestamp="Nil"
    else:
        average = latest.mode
        timestamp = latest.timestamp.isoformat(sep=' ', timespec='seconds')
    return render_template('index.html', number=average, timestamp=timestamp)