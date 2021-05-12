from model.group import Group


def test_edit_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(gr_name="Name changed"))
    app.session.logout()


def test_edit_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(gr_header="header changed"))
    app.session.logout()


def test_edit_first_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(gr_footer="footer changed"))
    app.session.logout()