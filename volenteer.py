import administrator
import additional_functions
from datetime import datetime


class Volunteer(administrator.Administrator):
    global total_collected_waste
    # date, waste collected
    total_collected_waste = []

    def say_hello(self):
        print(f"Hello from volunteer: lastname: {self.lastname}, name: {self.name}, birth year: {self.year_of_birth},"
              f" email: {self.email_address}, m.phone: {self.mobile_phone}, date created: {self.date_and_time_created},"
              f" address:\"{self.place_of_residence}\", photo: {self.photo}, is_admin: {self.is_administrator}")
    def add_information_about_collected_waste_in_day(self, type_of_waste, collected_weight, volume, the_day=datetime.now()):
        the_date = additional_functions.simple_date_format(the_day)
        density = round(collected_weight / volume, 3)
        if len(total_collected_waste) == 0:
            total_collected_waste.append({"date": the_date, "type of waste": type_of_waste, "collected waste": collected_weight,
                                          "volume": volume, "density": density})
        else:


                is_there_matching_date = any(day["date"] == the_date for day in total_collected_waste)
                if is_there_matching_date:
                    for day in total_collected_waste:
                        if day["date"] == additional_functions.simple_date_format(the_day):
                            day["type of waste"] = type_of_waste
                            day["collected waste"] += collected_weight
                            day["volume"] += volume
                            day["density"] = density
                            break
                else:
                    total_collected_waste.append({"date": the_date, "type of waste": type_of_waste, "collected waste": collected_weight,
                                          "volume": volume, "density": density})

                """
                #print(day)
                #print(len(total_collected_waste.py))
                print(day["date"] == additional_functions.simple_date_format(the_day), "is it true?")
                print(day["date"], additional_functions.simple_date_format(the_day), "Both dates side by side")
                print(total_collected_waste)
                if day["date"] == additional_functions.simple_date_format(the_day):
                    day["type of waste"] = type_of_waste
                    day["collected waste"] += collected_weight
                    day["volume"] += volume
                    day["density"] = density
                    #break
                else:
                    total_collected_waste.append({"date": the_date, "type of waste": type_of_waste, "collected waste": collected_weight,
                                          "volume": volume, "density": density})
                    #break
                    # day["date"] = the_date
                    # day["type of waste"] = type_of_waste
                    # day["collected waste"] += collected_weight
                    # day["volume"] += volume
                    # day["density"] = density
                """
    def get_data_about_collected_waste(self):
        for day in total_collected_waste:
            print(day)



