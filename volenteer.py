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
            total_collected_waste.append({"date": the_date, "type of waste": type_of_waste, "collected weight": collected_weight,
                                          "collected volume": volume, "density": density})
        else:
            is_there_matching_date = any(day["date"] == the_date for day in total_collected_waste)
            if is_there_matching_date:
                for day in total_collected_waste:
                    if day["date"] == additional_functions.simple_date_format(the_day):
                        day["type of waste"] = type_of_waste
                        day["collected weight"] += collected_weight
                        day["collected volume"] += volume
                        day["density"] = density
                        break
            else:
                total_collected_waste.append({"date": the_date, "type of waste": type_of_waste, "collected weight": collected_weight,
                                      "collected volume": volume, "density": density})

            """
            #print(day)
            #print(len(total_collected_waste.py))
            print(day["date"] == additional_functions.simple_date_format(the_day), "is it true?")
            print(day["date"], additional_functions.simple_date_format(the_day), "Both dates side by side")
            print(total_collected_waste)
            if day["date"] == additional_functions.simple_date_format(the_day):
                day["type of waste"] = type_of_waste
                day["collected weight"] += collected_weight
                day["collected volume"] += volume
                day["density"] = density
                #break
            else:
                total_collected_waste.append({"date": the_date, "type of waste": type_of_waste, "collected weight": collected_weight,
                                      "collected volume": volume, "density": density})
                #break
                # day["date"] = the_date
                # day["type of waste"] = type_of_waste
                # day["collected weight"] += collected_weight
                # day["collected volume"] += volume
                # day["density"] = density
            """
    def get_data_about_collected_waste(self):
        for day in total_collected_waste:
            print(day)

    def summary_of_waste_for_certain_period_of_time(self, volume_or_weight, waste_type, date_from, date_to):
        total_volume = 0
        total_weight = 0
        valid_waste_types = ["plastic", "glass", "paper"]
        if waste_type not in valid_waste_types:
            print("Please enter valid waste type: plastic, glass, paper")
        for day in total_collected_waste:
            #simple_date = additional_functions.simple_date_format(day["date"])
            date_format = additional_functions.create_datetime(day["date"])
            if date_format >= date_from and date_format <= date_to and day["type of waste"] == waste_type:
                if volume_or_weight == "volume":
                    total_volume += day["collected volume"]
                elif volume_or_weight == "weight":
                    total_weight += day["collected weight"]
                else:
                    print("Please enter 'volume_or_weight' = 'volume' or 'weight'")

        return total_volume if volume_or_weight == "volume" else total_weight

    def all_time_total_data(self):
        total_plastic_weight = 0
        total_glass_weight = 0
        total_paper_weight = 0

        total_plastic_volume = 0
        total_glass_volume = 0
        total_paper_volume = 0

        total_density = 0
        for day in total_collected_waste:
            if day["type of waste"] == "plastic":
                total_plastic_weight += day["collected weight"]
                total_plastic_volume += day["collected volume"]
            elif day["type of waste"] == "glass":
                total_glass_weight += day["collected weight"]
                total_glass_volume += day["collected volume"]
            elif day["type of waste"] == "paper":
                total_paper_weight += day["collected weight"]
                total_paper_volume += day["collected volume"]
            total_density += day["density"]

        total_all_types_weight = total_plastic_weight + total_glass_weight + total_paper_weight
        total_all_types_volume = total_plastic_volume + total_glass_volume + total_paper_volume
        print(f"total plastic weight: {total_plastic_weight}, total glass weight: {total_glass_weight},"
              f" total paper weight: {total_paper_weight}, total all types weight: {total_all_types_weight}"
              f"\ntotal plastic volume: {total_plastic_volume}, total glass volume: {total_glass_volume},"
              f" total paper volume: {total_paper_volume}, total all types volume: {total_all_types_volume}"
              f"\ntotal density: {round(total_density, 3)}")
