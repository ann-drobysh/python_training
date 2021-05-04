# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(gr_name="Test group", gr_header="test header", gr_footer="test footer"))
    app.session.logout()


def test_add_group_empty(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(gr_name="", gr_header="", gr_footer=""))
    app.session.logout()
