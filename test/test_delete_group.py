from model.group import Group


def test_delete_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete(Group(gr_title="Test group 1"))
    app.session.logout()
