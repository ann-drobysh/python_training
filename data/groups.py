from model.group import Group
import random
import string

constant = [
    Group(gr_name="name1", gr_header="header1", gr_footer="footer1"),
    Group(gr_name="name2", gr_header="header2", gr_footer="footer2")
]

'''
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(gr_name="", gr_header="", gr_footer="")] + [
    Group(gr_name=random_string("name", 5), gr_header=random_string("header", 10), gr_footer=random_string("footer", 10))
    for i in range(3)
]

'''