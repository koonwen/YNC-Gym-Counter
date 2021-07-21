import sqlite3

import click
from random import randint
from datetime import datetime
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('db/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


def reset_data_table():
    db = get_db()

    with current_app.open_resource('db/reset.sql') as f:
        db.executescript(f.read().decode('utf8'))

def mock_data(n=1):
    db = get_db()

    for i in range(n):
        db.execute('INSERT INTO data '
                   '(timestamp, img1, img2, img3, img4, img5, average)'
                   'VALUES (?, ?, ?, ?, ?, ?, ?)',
                   (datetime.now().isoformat(),
                    randint(0, 10),
                    randint(0, 10),
                    randint(0, 10),
                    randint(0, 10),
                    randint(0, 10),
                    randint(0, 10))
                    )
    db.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database')


@click.command('reset-data-table')
@with_appcontext
def reset_data_table_command():
    """Resets the data table and stores past data in a CSV"""
    reset_data_table()
    click.echo('Data table has been reset')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(reset_data_table_command)
