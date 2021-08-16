from model.group import Group
import random
import allure


def test_edit_some_group_name(app, db, check_ui):
    with allure.step("Given a groups list"):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(gr_name="Test group", gr_header="test header", gr_footer="test footer"))
        old_groups = db.get_group_list()
    with allure.step("Given a group from groups list"):
        group = random.choice(old_groups)
        index = old_groups.index(group)
    with allure.step("Given a data for group edit"):
        group_edited = Group(gr_name="Name changed")
    with allure.step("When I edit %s group" % group):
        app.group.edit_group_by_id(group.id, group_edited)
    with allure.step("Then the new list is equal to the old list with the edited group data"):
        new_groups = db.get_group_list()
        old_groups[index] = group_edited
        assert old_groups == new_groups
        if check_ui:
            def clean(group):
                return Group(id=group.id, gr_name=group.gr_name.strip())
            new_groups = map(clean, db.get_group_list())
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

'''def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(gr_name="Test group", gr_footer="test footer"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(gr_header="header changed"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(gr_name="Test group", gr_header="test header", gr_footer="test footer"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(gr_footer="footer changed"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)'''
