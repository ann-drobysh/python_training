from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(gr_title="changed 1", gr_name="changed 2", gr_header="header changed 2", gr_footer="footer changed 2"))
    app.session.logout()
