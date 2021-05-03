# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.Application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(gr_name="Test group", gr_header="test header", gr_footer="test footer"))
    app.session.logout()


def test_add_group_empty(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(gr_name="", gr_header="", gr_footer=""))
    app.session.logout()
