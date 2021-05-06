from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(gr_name="New test group", gr_header="test header", gr_footer="test footer"))
    app.group.edit(Group(gr_title="New test group", gr_name="Name changed", gr_header="header changed", gr_footer="footer changed"))
    app.session.logout()
