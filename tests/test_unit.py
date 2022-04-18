from flask import url_for
from flask_testing import TestCase
import pytest

from application import app, db
from application.models import Festivals


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLACHEMY_DATABASE_URI="sqlite:///test.db"
            SECRET_KEY="testsecretkey",
            WTF_CSRF_ENABLED=False
        )
        return app
    
    def setup(self):
        db.create_all()
        test = Festivals(Name='Test',Start_Date='01/01/2023', End_Date='02/01/2023')
        db.session.add(test)
        db.session.commit()

    def teardown(self):
        db.session.remove()
        db.drop_all()

class TestView(TestBase)
    def test_home_get(self):
        response = self.client.get(url_for('Home'))
        self.assertEqual(response.status_code, 200)


