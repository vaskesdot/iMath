from flask.cli import FlaskGroup

from project.__init__ import app, db

cli = FlaskGroup(app)


@cli.command("dev")
def dev():
    pass

# @cli.command("seed_db")
# def seed_initial_data_to_db():
#     seed_ecprice_data()


@cli.command("create_db")
def create_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.commit()


if __name__ == "__main__":
    cli()
