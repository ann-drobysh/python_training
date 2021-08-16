from model.contact import Contact
from model.group import Group
import random
import allure


def test_add_contact_to_group(app, dbORM):
    with allure.step("Given a contacts list"):
        old_contacts = dbORM.get_contact_list()
    with allure.step("Given a groups list"):
        old_groups = dbORM.get_group_list()
    if len(old_contacts) == 0:
        app.contact.add_new_contact(Contact(firstname="Testik", middlename="Midtest", lastname="Lasttest", nickname="Nickname test",
                                            title="Mrs", company="Test Company", street="5th Avenue", homephone="15", mobilephone="111999333", workphone="12123342", fax="2345645", email="test@test.com",
                                            birthday_day="11", birthday_month="July", birthday_year="1991", anniversary_day="8", anniversary_month="November", anniversary_year="1991", address2="Sec address", phone2="163434",
                                            note="testtesttest note"))
    if len(old_groups) == 0:
        app.group.create(Group(gr_name="Test group", gr_header="test header", gr_footer="test footer"))
    with allure.step("Given list of groups where not all existing contacts added"):
        available_groups = app.group.get_available_groups(old_groups, old_contacts, dbORM)
    with allure.step("Given random available group id"):
        group = random.choice(available_groups)
    with allure.step("Given contact that are not in group %s" % group):
        contacts_not_in_group = dbORM.get_contacts_not_in_group(group)
        contact = random.choice(contacts_not_in_group)
    with allure.step("When I add %s contact to the %s group" % (contact, group)):
        app.contact.add_contact_to_group(contact.id, group)
    with allure.step("Then the new list of contacts without groups is equal to the old list with the removed contact"):
        new_contacts_not_in_group = dbORM.get_contacts_not_in_group(group)
        contacts_not_in_group.remove(contact)
        assert contacts_not_in_group == new_contacts_not_in_group


