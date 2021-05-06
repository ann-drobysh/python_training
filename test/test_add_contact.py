# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.session.login("admin", "secret")
    app.contact.add_new_contact(Contact(firstname="Testik", middlename="Midtest", lastname="Lasttest", nickname="Nickname test", title="Mrs", company="Test Company", street="5th Avenue",
                                         home="15", mobilephone="111999333", workphone="12123342", fax="2345645", email="test@test.com", birthday_day="11",
                                         birthday_month="July", birthday_year="1991", anniversary_day="8",
                                         anniversary_month="November", anniversary_year="1991", address2="Sec address", phone2="163434", note="testtesttest note"))
    app.session.logout()


