import additional_functions
from datetime import datetime


class Administrator:
    def __init__(self, lastname, name, year_of_birth, email_address, mobile_phone,
                 place_of_residence, photo,):
        self.lastname = additional_functions.is_all_alphabetic(lastname)
        self.name = additional_functions.is_all_alphabetic(name)
        self.mobile_phone = additional_functions.correct_mobile_nr(mobile_phone)
        self.email_address = additional_functions.correct_email(email_address)
        self.place_of_residence = place_of_residence
        self._date_and_time_created = datetime.now()
        self.year_of_birth = additional_functions.correct_year_of_birth(year_of_birth)
        self.photo = photo

    @property
    def date_and_time_created(self):
        return self._date_and_time_created

    def hello_from_boss(self):
        print(f"Hello from: {self.lastname}, {self.year_of_birth}, {self.email_address}, {self.mobile_phone},"
              f" {self.date_and_time_created}, \"{self.place_of_residence}\", {self.photo}")

