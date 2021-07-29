import click
from app.db.models import db, Data
from flask.cli import with_appcontext


def init_db():
    db.drop_all()
    db.create_all()


def reset_data_table():
    db.session.query(Data).delete()
    db.session.commit()


def mock_db():
    db.drop_all()
    db.create_all()
    Data.mock_data(10)
    db.session.commit()


# ================================= CLI ==================================
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
    click.echo('Data table reset')


@click.command('mock-db')
@with_appcontext
def mock_db_command():
    """Resets the data table and stores past data in a CSV"""
    mock_db()
    click.echo('Mock data initialized')


def add_db_utils(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(reset_data_table_command)
    app.cli.add_command(mock_db_command)