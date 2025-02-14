from app.models.planet import Planet
import pytest
from app import create_app
from app import db


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_saved_planets(app):
    neptune = Planet(name="Neptune", description="no surface")
    mars = Planet(name="Mars", description="elon")

    db.session.add_all([neptune, mars])
    db.session.commit()
