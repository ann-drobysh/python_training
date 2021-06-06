from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1", nickname="nickname1",
            title="title1", company="companyname1", street="street1",
            birthday_day="15", birthday_month="July", birthday_year="1978", anniversary_day="20",
            anniversary_month="November", anniversary_year="1996",
            homephone="11111111", mobilephone="1111112", workphone="111113", fax="111114", email="test1@test.com",
            address2="secondaddress1", phone2="11111115", note="note1"),
    Contact(firstname="firstname2", middlename="middlename2", lastname="lastname2", nickname="nickname2",
            title="title2", company="companyname2", street="street2",
            birthday_day="15", birthday_month="July", birthday_year="1978", anniversary_day="20",
            anniversary_month="November", anniversary_year="1996",
            homephone="2222221", mobilephone="2222222", workphone="222223", fax="2222224", email="test2@test.com",
            address2="secondaddress2", phone2="2222225", note="note2")
]

'''
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_phones(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_emails(maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                    title="", company="", street="",
                    birthday_day="", birthday_month="", birthday_year="", anniversary_day="",
                    anniversary_month="", anniversary_year="",
                    homephone="", mobilephone="", workphone="", fax="", email="",
                    address2="", phone2="",
                    note="")] + [
    Contact(firstname=random_string("fname", 10),  middlename=random_string("mname", 10), lastname=random_string("lname", 10),
          nickname=random_string("nick", 10), title=random_string("t", 5), company=random_string("comp", 10),
          street=random_string("address", 10), homephone=random_string_phones(10), mobilephone=random_string_phones(10),
          workphone=random_string_phones(10), fax=random_string_phones(10), email=random_string_emails(10)+"@test.com",
          birthday_day="11", birthday_month="July", birthday_year="1991", anniversary_day="8",
          anniversary_month="November", anniversary_year="1991", address2=random_string("addr2", 10), phone2=random_string_phones(10),
          note=random_string("note", 20))
    for i in range(3)
]
'''