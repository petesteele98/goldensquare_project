from datetime import datetime




class Birthdates:

    birthday_dictionary = {}

    def __init__(self):
        pass

    def add_birthday(self, name, birthday):
        # take a name and date and add it to the birthday dictionary
        birthday_date_format = datetime.strptime(birthday, '%d/%m/%Y').date()
        self.birthday_dictionary[name] = birthday_date_format
        return f"{name}'s birthday has been added to the list. The list is now: {self.birthday_dictionary}"
        
 

    # def check_age(birthday):
    #     try:
    #         birth_day = datetime.strptime(birthday, '%Y-%m-%d')
    #     except ValueError:
    #         raise ValueError("Incorrect data format, should be YYYY-MM-DD.")
    #     now = datetime.today()
    #     age = relativedelta(now, birth_day).years
    #     if age > 16:
    #         return 'access has been granted.'



        

    def update_birthdate(self, name, newdate):
        self.birthday_dictionary.update({name: newdate})
        return f"{name}'s birthday has been updated. The list is now: {self.birthday_dictionary}"


    def update_name(self, name, newname):
        self.birthday_dictionary[newname] = self.birthday_dictionary[name]
        del self.birthday_dictionary[name]
        return f"The name {name} has been replaced with {newname}. The list is now: {self.birthday_dictionary}"
    
# Note: Coaches : is it a problem that our tests have to run in a specific order? Ie: the update_name test would not work
# if it ran before the add_birthday test.
  
    def birthdays_approaching(self):
        pass
    #     ## Parameters: name (string), newname(string)
    #     ## side effects: none
    # Needs to get todays date:
        today = datetime.today()
    # Then go through the key value pairs in the dictionary (for loop)
    # and IF the value of the key (the date of the birthday) is with in the next 30 days it needs to be added to new dictionary
    # then return the dictionary to show the birthdays coming up!





    
    def age_appropriate(self, name):
        pass
    #     ## Parameters: name (string)
    #     ## side effects: none

    def update_status(self, name, status):
        pass
    #     ## Parameters: name (string) , status(string)
    #     ## side effects: none

    def check_status(self, name):
        pass




# bonus things:
# sort out the list formatting to remove the {}
# sort out the return format of the date function 


birthday = Birthdates()

print(birthday.add_birthday('Sam', '02/04/1990'))


print(type((birthday.add_birthday('Sam', '02/04/1990'))))


print(type('skjdhsdh'))