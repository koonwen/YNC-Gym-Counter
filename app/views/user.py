from flask import Blueprint, render_template
from app.db.models import Data
bp = Blueprint('user', __name__)

# This view returns the maximum number of people recorded in the gym over a 5 minute interval
# The number is multiplied by 2 to better estimate the actual number of people given the constraints of the
# camera set up
@bp.route('/')
def index():
    latest5 = Data.get_latest_n_entries(5)
    if not latest5:
        highest="No data yet"
        timestamp="Nil"
    else:
        hi_list = map(lambda entry: entry.highest, latest5)
        highest = max(hi_list) * 2
        timestamp = latest5[4].timestamp.isoformat(sep=' ', timespec='seconds')
    return render_template('index.html', number=highest, timestamp=timestamp)