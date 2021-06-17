from flask import Blueprint, render_template, request
from app.auth import login_required
from app.db import get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
@login_required
def index():
    db = get_db()
    table = db.execute('SELECT * FROM data LIMIT 10').fetchall()
    return render_template('admin.html', table=table)


@bp.route('/addtime', methods=['POST'])
@login_required
def add_data():
    data = request.get_json()
    timestamp = data["timestamp"]
    img1, img2, img3, img4, img5 = data["img1"], data["img2"], data["img3"], data["img4"], data['img5']
    average = (img1 + img2 + img3 + img4 + img5) // 5

    db = get_db()
    db.execute('INSERT INTO data (timestamp, img1, img2, img3, img4, img5, average) '
               'VALUES (?,?,?,?,?,?,?)',
               (timestamp, img1, img2, img3, img4, img5, average))
    db.commit()
    return "Success"


@bp.route('/pi', methods=['POST'])
def receive_data():
    data = request.get_json()
    db = get_db()
    db.execute('INSERT INTO data (timestamp, img1, img2, img3, img4, img5, average)'
               'VALUES (?, ?, ?, ?, ?, ?, ?)',
               (data['timestamp'], data['img1'], data['img2'], data['img3'], data['img4'], data['img5'], data['average']))
    db.commit()
    return "Success"
