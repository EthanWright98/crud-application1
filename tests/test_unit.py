from flask import url_for
from flask_testing import TestCase
import pytest
from flask_sqlalchemy import SQLAlchemy

from application import app, db
from application.models import Festivals, Stages


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLACHEMY_DATABASE_URI="mysql+pymysql://root:letmein1234@10.126.96.3/crudapp1",
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

class TestView(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('New_Festival'))
        self.assertEqual(response.status_code, 200)

    def setup(self):
        db.create_all()
        test = Stages(Name='Stage1', Festival_id='1')
        db.session.add(test)
        db.session.commit()

    def teardown(self):
        db.session.remove()
        db.drop_all()

class TestVeiw(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('Add_Stage'))
        self.assertEqual(response.status_code, 200)

class TestUpdate(TestBase):
    def test_home_edit(self):
        response = self.client.post(
            url_for('update', id=1),
            data = dict(Name='test2', Start_Date='01/01/2023', End_Date='03/01/2023'
            ),
            follow_redirects = True
        )
        self.assertNotIn(b'test2', response.data)

    def test_delete(self):
        response = self.client.delete(url_for('delete',id=1))
        self.assertNotIn(b'Name', response.data)









