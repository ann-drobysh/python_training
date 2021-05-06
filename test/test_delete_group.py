from model.group import Group


def test_delete_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(gr_name="Test delete group", gr_header="test header", gr_footer="test footer"))
    app.group.delete(Group(gr_title="Test delete group"))
    app.session.logout()
