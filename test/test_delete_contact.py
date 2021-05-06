from model.contact import Contact

def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
# personal_name parameter value format: Firstname Lastname
    app.contact.delete_contact(Contact(personal_name="Testik edit Lasttest edit"))
    app.session.logout()
