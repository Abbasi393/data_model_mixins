import click
from flask_script import Manager
from demo.seeds import insert_demo_data
from app import app

manager = Manager(app)


@app.cli.command()
def seed_data():
    """Insert demo data for testing."""
    insert_demo_data()
    click.echo('Demo data inserted.')


if __name__ == '__main__':
    manager.run()
