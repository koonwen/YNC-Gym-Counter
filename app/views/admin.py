from flask import Blueprint, render_template, request
from app.views.auth import login_required
from app.db import db, Data
bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
@login_required
def index():
    table = Data.query.order_by(Data.timestamp.desc()).limit(10)
    return render_template('admin.html', table=table)

# TODO Add some validation
#TODO Change average to mode on raspberry pi end
@bp.route('/pi', methods=['POST'])
def receive_data():
    """Endpoint to receive data from Pi"""
    data = request.get_json()
    d = Data(timestamp=data['timestamp'],
         img1=data['img1'],
         img2=data['img2'],
         img3=data['img3'],
         img4=data['img4'],
         img5=data['img5'],
         mode=data['average'])
    db.session.add(d)
    db.session.commit()
    return "Success"
