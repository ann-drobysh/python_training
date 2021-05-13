# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(gr_name="Test group", gr_header="test header", gr_footer="test footer"))

def test_add_group_empty(app):
    app.group.create(Group(gr_name="", gr_header="", gr_footer=""))
