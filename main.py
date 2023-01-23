import administrator
import volenteer
from datetime import datetime


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#boss1 = administrator.Administrator("Zigbumbulis")


helper = volenteer.Volunteer("Mitina", "Dace", 1983, "Dace@gmail.com", "+371 20063111",
                                    "Rīga, Madagaskaras iela 456-5100", "/photos/dace_mitina.jpg", False)

boss = administrator.Administrator("Mītins", "Kristaps", 1987, "kristaps@gmail.com", "+371 82850111",
                                    "Rīga, Kapsēdes iela 456-5100", "/photos/kristaps_mitins.jpg", True)

helper.add_information_about_collected_waste_in_day("plastic", 1, 3, datetime(2020, 12, 24))
helper.add_information_about_collected_waste_in_day("plastic", 1, 3, datetime(2020, 12, 24))
helper.add_information_about_collected_waste_in_day("plastic", 2, 6)
helper.add_information_about_collected_waste_in_day("glass", 4, 8, datetime(2018, 1, 1))
helper.add_information_about_collected_waste_in_day("plastic", 2, 6)
helper.add_information_about_collected_waste_in_day("glass", 4, 8, datetime(2018, 1, 1))
helper.add_information_about_collected_waste_in_day("paper", 2, 3, datetime(2021, 12, 31))
helper.add_information_about_collected_waste_in_day("plastic", 2, 6)
helper.add_information_about_collected_waste_in_day("glass", 4, 8, datetime(2018, 1, 1))

helper.add_information_about_collected_waste_in_day("paper", 2, 3, datetime(2021, 12, 31))
helper.add_information_about_collected_waste_in_day("paper", 2, 3, datetime(2021, 12, 31))

helper.add_information_about_collected_waste_in_day("plastic", 2, 6)

helper.add_information_about_collected_waste_in_day("plastic", 1, 3, datetime(2020, 12, 24))
helper.add_information_about_collected_waste_in_day("plastic", 1, 3, datetime(2020, 12, 24))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    #boss.date_and_time_created = "MOTHER FUCKER!"
    #boss.say_hello()
    #helper.date_and_time_created = "MOTHER FUCKER!"
    #helper.say_hello()
    print(boss.get_fullname())
    print(helper.get_fullname())

    helper.get_data_about_collected_waste()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
