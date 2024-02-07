class Birthdates:

    def __init__(self):
        self.birthday_list = {}
    ## Parameters: name (string), birthday (string)
    ##  side effects: none 

    def add_birthday(self, name, birthday):
      # parameters: 
        # name : string
        # birthday : string
    

    def update_birthday(self, name, newdate):
        
    #     ## Parameters: name (string), newdate(string)
    #     ## side effects: none

    def update_name(self, name, newname):
        
    #     ## Parameters: name (string), newname(string)
    #     ## side effects: none
    def birthdays_approaching(self):
        
    #     ## Parameters: name (string), newname(string)
    #     ## side effects: none
    
    def age_appropriate(self, name):
    
    #     ## Parameters: name (string)
    #     ## side effects: none

    def status(self, name, status):

    #     ## Parameters: name (string) , status(string)
    #     ## side effects: none



birthday = Birthdates()

birthday.add('Josh', '11-12-1997')


def test_add_birthday():
    birthday = Birthdates('Pete', '14-12-1998')
    assert result == "Pete's birthday has been added to the list! Here is the list: "


def test_update_birthday():
    birthday = Birthdates('Josh', '11-12-1997')
    birthday.update_birthday('Rosie', '04-02-1989')
    assert result == {'Josh':'11-12-1997', 'Rosie':'04-02-1989'}



