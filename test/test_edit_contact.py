from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(firstname="Testik", middlename="Midtest", lastname="Lasttest", nickname="Nickname test",
                                            title="Mrs", company="Test Company", street="5th Avenue", homephone="15", mobilephone="111999333", workphone="12123342", fax="2345645", email="test@test.com",
                                            birthday_day="11", birthday_month="July", birthday_year="1991", anniversary_day="8", anniversary_month="November", anniversary_year="1991", address2="Sec address", phone2="163434",
                                            note="testtesttest note"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Test edit", middlename="Midtest edit", lastname="Lasttest edit", nickname="Nickname test edit", title="Mrs edit", company="Test Company edit", street="5th Avenue edit",
                      homephone="15 edit", mobilephone="111999333444", workphone="12123342444", fax="2345645444", email="testedit@test.com", birthday_day="1",
                      birthday_month="August", birthday_year="1990", anniversary_day="1",
                      anniversary_month="October", anniversary_year="1990", address2="Sec address edit", phone2="163434444", note="testtesttest note edit")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)