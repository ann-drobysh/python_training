from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(gr_name="Name changed", gr_header="header changed", gr_footer="footer changed"))
    app.session.logout()
