from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(gr_name="Test group", gr_header="test header", gr_footer="test footer"))
    app.group.edit_first_group(Group(gr_name="Name changed"))


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(gr_name="Test group", gr_footer="test footer"))
    app.group.edit_first_group(Group(gr_header="header changed"))


def test_edit_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(gr_name="Test group", gr_header="test header", gr_footer="test footer"))
    app.group.edit_first_group(Group(gr_footer="footer changed"))
