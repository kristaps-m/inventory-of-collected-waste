import administrator
from datetime import datetime
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#boss1 = administrator.Administrator("Mitins")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    boss2 = administrator.Administrator("Mītins", "Kristaps", 1987, "kristaps@gmail.com", "+371 82850485",
                                        datetime.now(), "Rīga, Kapsēdes iela 456-5100", "/photos/kristaps_mitins.jpg")
    #boss1.hello_from_boss()
    boss2.hello_from_boss()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
