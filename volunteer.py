import administrator
import additional_functions
from datetime import *


class Volunteer(administrator.Administrator):
    def __init__(self, lastname, name, year_of_birth, email_address, mobile_phone, place_of_residence, photo,
                 is_administrator):
        self.total_collected_waste = []
        super().__init__(lastname, name, year_of_birth, email_address, mobile_phone, place_of_residence, photo,
                         is_administrator)

    def say_hello(self):
        print(f"Hello from volunteer: lastname: {self.lastname}, name: {self.name}, birth year: {self.year_of_birth},"
              f" email: {self.email_address}, m.phone: {self.mobile_phone}, date created: {self.date_and_time_created},"
              f" address:\"{self.place_of_residence}\", photo: {self.photo[:5]}..., is_admin: {self.is_administrator}")

    def add_information_about_collected_waste_in_day(self, type_of_waste, collected_weight, collected_volume,
                                                     the_day=datetime.now()):
        valid_waste_types = ["plastic", "glass", "paper"]
        if type_of_waste not in valid_waste_types:
            print("Please enter valid waste type: plastic, glass, paper")
        the_date = additional_functions.simple_date_format(the_day)
        density = round(collected_weight / collected_volume, 3)
        is_there_matching_date = any(day["date"] == the_date for day in self.total_collected_waste)

        if is_there_matching_date:
            for day in self.total_collected_waste:
                if day["date"] == additional_functions.simple_date_format(the_day):
                    day["the waste"][type_of_waste]["weight"] += collected_weight
                    day["the waste"][type_of_waste]["volume"] += collected_volume
                    day["the waste"][type_of_waste]["density"] = density
        else:
            the_appendable_object = {"date": the_date, "the waste": {
                "plastic": {"weight": 0, "volume": 0, "density": 0},
                "glass": {"weight": 0, "volume": 0, "density": 0},
                "paper": {"weight": 0, "volume": 0, "density": 0},
            }}

            if type_of_waste == "plastic":
                the_appendable_object["the waste"]["plastic"]["weight"] = collected_weight
                the_appendable_object["the waste"]["plastic"]["volume"] = collected_volume
                the_appendable_object["the waste"]["plastic"]["density"] = density
            elif type_of_waste == "glass":
                the_appendable_object["the waste"]["glass"]["weight"] = collected_weight
                the_appendable_object["the waste"]["glass"]["volume"] = collected_volume
                the_appendable_object["the waste"]["glass"]["density"] = density
            elif type_of_waste == "paper":
                the_appendable_object["the waste"]["paper"]["weight"] = collected_weight
                the_appendable_object["the waste"]["paper"]["volume"] = collected_volume
                the_appendable_object["the waste"]["paper"]["density"] = density

            self.total_collected_waste.append(the_appendable_object)

    def data_about_collected_waste_for_each_day(self):
        for day in self.total_collected_waste:
            print(str(day)[1:-1])

    def summary_of_waste_for_certain_period_of_time(self, volume_or_weight, waste_type, date_from, date_to):
        total_volume = 0
        total_weight = 0
        valid_waste_types = ["plastic", "glass", "paper"]
        if waste_type not in valid_waste_types:
            print("Please enter valid waste type: plastic, glass, paper")
        if volume_or_weight not in ["weight", "volume"]:
            print("Please enter 'volume_or_weight' = 'volume' or 'weight'")
        for day in self.total_collected_waste:
            # simple_date = additional_functions.simple_date_format(day["date"])
            date_format = additional_functions.create_datetime(day["date"])
            if date_format >= date_from and date_format <= date_to:
                total_volume += day["the waste"][waste_type]["volume"]
                total_weight += day["the waste"][waste_type]["weight"]

        return total_volume if volume_or_weight == "volume" else total_weight

    def all_time_total_data(self):
        total_plastic_weight = 0
        total_glass_weight = 0
        total_paper_weight = 0

        total_plastic_volume = 0
        total_glass_volume = 0
        total_paper_volume = 0

        total_density = 0
        for day in self.total_collected_waste:
            total_plastic_weight += day["the waste"]["plastic"]["weight"]
            total_plastic_volume += day["the waste"]["plastic"]["volume"]

            total_glass_weight += day["the waste"]["glass"]["weight"]
            total_glass_volume += day["the waste"]["glass"]["volume"]

            total_paper_weight += day["the waste"]["paper"]["weight"]
            total_paper_volume += day["the waste"]["paper"]["volume"]
            total_density += sum([day["the waste"]["plastic"]["density"], day["the waste"]["glass"]["density"],
                                  day["the waste"]["paper"]["density"]])

        total_all_types_weight = total_plastic_weight + total_glass_weight + total_paper_weight
        total_all_types_volume = total_plastic_volume + total_glass_volume + total_paper_volume

        print(f"total plastic weight: {total_plastic_weight}, total glass weight: {total_glass_weight},"
              f" total paper weight: {total_paper_weight}, total all types weight: {total_all_types_weight}"
              f"\ntotal plastic volume: {total_plastic_volume}, total glass volume: {total_glass_volume},"
              f" total paper volume: {total_paper_volume}, total all types volume: {total_all_types_volume}"
              f"\ntotal density: {round(total_density, 3)}")
