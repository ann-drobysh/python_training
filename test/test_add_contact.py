# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_phones(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_emails(maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                    title="", company="", street="",
                    birthday_day="", birthday_month="", birthday_year="", anniversary_day="",
                    anniversary_month="", anniversary_year="",
                    homephone="", mobilephone="", workphone="", fax="", email="",
                    address2="", phone2="",
                    note="")] + [
    Contact(firstname=random_string("fname", 10),  middlename=random_string("mname", 10), lastname=random_string("lname", 10),
          nickname=random_string("nick", 10), title=random_string("t", 5), company=random_string("comp", 10),
          street=random_string("address", 10), homephone=random_string_phones(10), mobilephone=random_string_phones(10),
          workphone=random_string_phones(10), fax=random_string_phones(10), email=random_string_emails(10)+"@test.com",
          birthday_day="11", birthday_month="July", birthday_year="1991", anniversary_day="8",
          anniversary_month="November", anniversary_year="1991", address2=random_string("addr2", 10), phone2=random_string_phones(10),
          note=random_string("note", 20))
    for i in range(3)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


