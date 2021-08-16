import random
from model.contact import Contact
from model.group import Group
import allure

def test_delete_contact_from_group(app, dbORM):
    with allure.step("Given a non-empty list of groups with contact"):
        if len(dbORM.get_contact_list()) == 0:
            app.contact.add_new_contact(
                Contact(firstname="Testik", middlename="Midtest", lastname="Lasttest", nickname="Nickname test",
                        title="Mrs", company="Test Company", street="5th Avenue", homephone="15",
                        mobilephone="111999333", workphone="12123342", fax="2345645", email="test@test.com",
                        birthday_day="11", birthday_month="July", birthday_year="1991", anniversary_day="8",
                        anniversary_month="November", anniversary_year="1991", address2="Sec address", phone2="163434",
                        note="testtesttest note"))
        if len(dbORM.get_group_list()) == 0:
            app.group.create(Group(gr_name="Test group", gr_header="test header", gr_footer="test footer"))
        if len(dbORM.get_groups_with_contacts()) == 0:
            group = random.choice(dbORM.get_group_list())
            contact = random.choice(dbORM.get_contact_list())
            app.contact.add_contact_to_group(contact.id, group)
        groups_with_contacts = dbORM.get_groups_with_contacts()
    with allure.step("Given a group with added contacts"):
        group = random.choice(groups_with_contacts)
    with allure.step("Given a list of contacts in %s group" % group):
        contacts_in_group = dbORM.get_contacts_in_groups(group)
    with allure.step("Given contact from %s group" % group):
        contact = random.choice(contacts_in_group)
    with allure.step("When I delete contact %s from the %s group" % (contact, group)):
        app.contact.delete_contact_from_group(contact.id, group)
    with allure.step("Then the new list is equal to the old list with the removed contact"):
        new_contacts_in_group = dbORM.get_contacts_in_groups(group)
        contacts_in_group.remove(contact)
        assert contacts_in_group == new_contacts_in_group







