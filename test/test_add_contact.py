# -*- coding: utf-8 -*-
from model.contact import Contact
import allure

def test_add_new_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    with allure.step("Given a contacts list"):
        old_contacts = db.get_contacts_list()
    with allure.step("When I add contact %s to the list" % contact):
        app.contact.add_new_contact(contact)
    with allure.step("Then the new list is equal to the old list with the added contact"):
        new_contacts = db.get_contacts_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            def clean(contact):
                return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
            new_contacts = map(clean, db.get_contacts_list())
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)


