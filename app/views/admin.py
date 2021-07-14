from flask import Blueprint, render_template, request
from app.views.auth import login_required
from app.db.utils import get_db
bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
@login_required
def index():
    db = get_db()
    table = db.execute('SELECT * FROM data '
                       'ORDER BY timestamp DESC LIMIT 10').fetchall()
    return render_template('admin.html', table=table)

# TODO Add some validation
@bp.route('/pi', methods=['POST'])
def receive_data():
    """Endpoint to receive data from the Raspberry pi"""
    data = request.get_json()
    db = get_db()
    db.execute('INSERT INTO data (timestamp, img1, img2, img3, img4, img5, average)'
               'VALUES (?, ?, ?, ?, ?, ?, ?)',
               (data['timestamp'], data['img1'], data['img2'], data['img3'], data['img4'], data['img5'], data['average']))
    db.commit()
    return "Success"
