class Administrator:
    def __init__(self, lastname, name, year_of_birth, email_address, mobile_phone,
                 date_and_time_created, place_of_residence, photo):
        self.lastname = lastname
        self.name = name
        self.mobile_phone = mobile_phone
        self.email_address = email_address
        self.place_of_residence = place_of_residence
        self.date_and_time_created = date_and_time_created
        self.year_of_birth = year_of_birth
        self.photo = photo


    def hello_from_boss(self):
        print(f"Hello from: {self.lastname} {self.year_of_birth}, {self.email_address}, {self.mobile_phone},"
              f" {self.date_and_time_created}, \"{self.place_of_residence}\", {self.photo}")

