# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.app_add_contact import AddNewContact


@pytest.fixture
def app(request):
    fixture = AddNewContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.login("admin", "secret")
    app.add_new_contact(Contact(firstname="Test", middlename="Midtest", lastname="Lasttest", nickname="Nickname test", title="Mrs", company="Test Company", street="5th Avenue",
                                         home="15", mobilephone="111999333", workphone="12123342", fax="2345645", email="test@test.com", birthday_day="11",
                                         birthday_month="July", birthday_year="1991", anniversary_day="8",
                                         anniversary_month="November", anniversary_year="1991", address2="Sec address", phone2="163434", note="testtesttest note"))
    app.logout()


