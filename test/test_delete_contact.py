from model.contact import Contact

def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new_contact(Contact(firstname="Anna", lastname="Test"))

# personal_name parameter value format: Firstname Lastname
    app.contact.delete_contact(Contact(personal_name="Anna Test"))
    app.session.logout()
