import administrator
import volunteer
import dummy_data
from datetime import *

"""Example Administrator"""
boss = administrator.Administrator("Mītins", "Kristaps", 1987, "kristaps@gmail.com", "+371 82850111",
                                   "Rīga, Kapsēdes iela 456-5100", "https://picsum.photos/200/300", True)

"""Example Volunteers"""
helper1 = volunteer.Volunteer("Berzina", "Liene", 1983, "liene@gmail.com", "+371 20063111",
                             "Rīga, Madagaskaras iela 456-5100", "https://picsum.photos/200/300", False)

helper2 = volunteer.Volunteer("Ozols", "Girts", 15.5, "Girts.Ozols", "+371 25563111",
                             "Ventspils, Brivibas iela 456-5100", "https://picsum.photos/200/300", False)

"""Example Administrator adding collected waste data for each volunteer"""
for one_day in dummy_data.list_of_volunteer_data1:
    helper1.add_information_about_collected_waste_in_day(*one_day)

for one_day in dummy_data.list_of_volunteer_data2:
    helper2.add_information_about_collected_waste_in_day(*one_day)


if __name__ == '__main__':
    print(boss.get_fullname())

    print(helper1.get_fullname())
    helper1.data_about_collected_waste_for_each_day()
    print(helper1.summary_of_waste_for_certain_period_of_time("volume", "plastic", datetime(2020, 12, 1), datetime.now()))
    print(helper1.summary_of_waste_for_certain_period_of_time("weight", "plastic", datetime(2023, 1, 23), datetime(2023, 1, 25)))
    helper1.all_time_total_data()
    #helper1.save_photo()

    print(helper2.get_fullname())
    helper2.data_about_collected_waste_for_each_day()
    print(helper2.summary_of_waste_for_certain_period_of_time("weight", "plastic", datetime(2000, 1, 1), datetime(2019, 12, 31)))
    print(helper2.summary_of_waste_for_certain_period_of_time("volume", "paper", datetime(2021, 1, 1), datetime(2021, 12, 31)))
    helper2.all_time_total_data()
    #helper2.save_photo()

