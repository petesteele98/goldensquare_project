
from lib.birthdates_class import *


def test_add_birthday():
    birthday = Birthdates()
    result = birthday.add_birthday('Pete', '14/12/1998')
    assert result == "Pete's birthday has been added to the list. The list is now: {'Pete': '14/12/1998'}"


def test_update_birthdate():
    birthday = Birthdates()
    birthday.add_birthday('Pete', '18-04-1984')
    result = birthday.update_birthdate('Pete', '14-12-1998')
    assert result == "Pete's birthday has been updated. The list is now: {'Pete': '14-12-1998'}"


def test_update_name():
    birthday = Birthdates()
    birthday.add_birthday('Jush', '11-12-1997')
    result = birthday.update_name('Jush', 'Josh')
    assert result == "The name Jush has been replaced with Josh. The list is now: {'Pete': '14-12-1998', 'Josh': '11-12-1997'}"


def test_birthdays_approaching():
    birthday = Birthdates()
    birthday.add_birthday('Steve', '11-02-1997')
    birthday.add_birthday('San', '04-03-1997')
    birthday.add_birthday('Thea', '01-03-1997')
    result = birthday.birthdays_approaching()
    assert result == "These are the birthdays coming up in the next month: 'Steve': '11-02-1997', 'San': '04-03-1997','Thea':'01-03-1997'"


def test_age_appropriate():
    birthday = Birthdates()
    birthday.add_birthday('Steve', '11-02-1987')
    birthday.add_birthday('San', '04-03-1991')
    birthday.add_birthday('Thea', '01-03-2018')
    result = birthday.age_appropriate('Thea')
    assert result == 'Thea will be 6 years old. Make sure you buy a cute card for a child!'


def test_age_appropriate():
    birthday = Birthdates()
    birthday.add_birthday('Steve', '11-02-1987')
    birthday.add_birthday('San', '04-03-1991')
    birthday.add_birthday('Thea', '01-03-2018')
    result = birthday.age_appropriate('Steve')
    assert result == 'Steve will be 37 years old. He is very old, make sure you buy him an offensive card!'


def test_age_appropriate():
    birthday = Birthdates()
    birthday.add_birthday('Steve', '11-02-1987')
    birthday.add_birthday('San', '07-03-1995')
    birthday.add_birthday('Thea', '01-03-2018')
    result = birthday.age_appropriate('San')
    assert result == 'San will be 29 years old. Make sure you buy a lovely card!'

def test_update_status():
    birthday = Birthdates()
    birthday.add_birthday('Valentine', '07-03-1995')
    result = birthday.update_status('Valentine', 'sent')
    assert result == "Valentine's birthday card status has been updated to 'sent'"

def test_check_status():
    birthday = Birthdates()
    birthday.add_birthday('Valentine', '07-03-1995')
    result = birthday.check_status('Valentine')
    assert result == "Valentine's birthday card status is 'not sent'"


def test_check_status1():
    birthday = Birthdates()
    birthday.add_birthday('Jess', '07-03-1995')
    result = birthday.update_status('Jess', 'sent')
    result = birthday.check_status('Jess')
    assert result == "Jess's birthday card status is 'sent'"