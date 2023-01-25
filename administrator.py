import base64
import additional_functions
from datetime import *


class Administrator:
    def __init__(self, lastname, name, year_of_birth, email_address, mobile_phone,
                 place_of_residence, photo, is_administrator):
        self.lastname = lastname if additional_functions.is_all_alphabetic(lastname) else "-UNDEFINED-"
        self.name = name if additional_functions.is_all_alphabetic(name) else "-UNDEFINED-"
        self.year_of_birth = additional_functions.correct_year_of_birth(year_of_birth)
        self.email_address = additional_functions.correct_email(email_address)
        self.mobile_phone = additional_functions.correct_mobile_nr(mobile_phone)
        self.place_of_residence = place_of_residence
        self._date_and_time_created = datetime.now()
        self.photo = additional_functions.from_url_save_picture_as_base64(photo)
        self.is_administrator = is_administrator

    @property
    def date_and_time_created(self):
        return self._date_and_time_created

    def get_fullname(self):
        return f"<{self.name.title()} {self.lastname.title()}> {self.email_address}"

    def say_hello(self):
        print(f"Hello from administrator: lastname: {self.lastname}, name: {self.name}, birth year: {self.year_of_birth},"
              f" email: {self.email_address}, m.phone: {self.mobile_phone}, date created: {self.date_and_time_created},"
              f" address:\"{self.place_of_residence}\", photo: {self.photo[:5]}..., is_admin: {self.is_administrator}")

    def save_photo(self):
        with open(f"foto_{self.name}_{self.lastname}.jpg", "wb") as new_file:
            new_file.write(base64.decodebytes(self.photo))
        print(f"Picture saved as 'foto_{self.name}_{self.lastname}.jpg'")

