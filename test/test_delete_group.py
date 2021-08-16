from model.group import Group
import random
import allure

def test_delete_some_group(app, db, check_ui):
    with allure.step("Given a groups list"):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(gr_name="Test group", gr_header="test header", gr_footer="test footer"))
        old_groups = db.get_group_list()
    with allure.step("Given a group from groups list"):
        group = random.choice(old_groups)
    with allure.step("When I delete group %s from the list" % group):
        app.group.delete_group_by_id(group.id)
    #assert len(old_groups) - 1 == app.group.count()
    with allure.step("Then the new list is equal to the old list with the removed group"):
        new_groups = db.get_group_list()
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            def clean(group):
                return Group(id=group.id, gr_name=group.gr_name.strip())
            new_groups = map(clean, db.get_group_list())
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
