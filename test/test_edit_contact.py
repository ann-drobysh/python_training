from model.contact import Contact

def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
# personal_name parameter value format: Firstname Lastname
    app.contact.edit_contact(Contact(personal_name="Testik Lasttest", firstname="Testik edit", middlename="Midtest edit", lastname="Lasttest edit", nickname="Nickname test edit", title="Mrs edit", company="Test Company edit", street="5th Avenue edit",
                                         home="15 edit", mobilephone="111999333444", workphone="12123342444", fax="2345645444", email="testedit@test.com", birthday_day="1",
                                         birthday_month="August", birthday_year="1990", anniversary_day="1",
                                         anniversary_month="October", anniversary_year="1990", address2="Sec address edit", phone2="163434444", note="testtesttest note edit"))
    app.session.logout()
