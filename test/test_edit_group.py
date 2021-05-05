from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(gr_title="abc", new_gr_name="changed", new_gr_header="header changed", new_gr_footer="footer changed"))
    app.session.logout()
