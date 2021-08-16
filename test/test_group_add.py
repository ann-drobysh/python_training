# -*- coding: utf-8 -*-
from model.group import Group
import allure

def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step("Given a groups list"):
        old_groups = db.get_group_list()
    with allure.step("When I add group %s to the list" % group):
        app.group.create(group)
    with allure.step("Then the new list is equal to the old list with the added group"):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            def clean(group):
                return Group(id=group.id, gr_name=group.gr_name.strip())
            new_groups = map(clean, db.get_group_list())
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

