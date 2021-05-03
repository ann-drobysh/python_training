# -*- coding: utf-8 -*-
import pytest
from group import Group
from app_add_group import AddGroupApp


@pytest.fixture
def app(request):
    fixture = AddGroupApp()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(gr_name="Test group", gr_header="test header", gr_footer="test footer"))
    app.logout()


def test_add_group_empty(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(gr_name="", gr_header="", gr_footer=""))
    app.logout()
