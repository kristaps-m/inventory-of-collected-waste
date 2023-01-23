import base64
import datetime


def is_whole(n):
    return n % 1 == 0


def correct_year_of_birth(year_of_birth):
    if year_of_birth > 0 and is_whole(year_of_birth):
        return year_of_birth

    return 2000


def correct_email(email):
    if '@' in email:
        return email

    return email + "@gmail.com"


def correct_mobile_nr(mobile):
    return "".join(i for i in mobile if i.isdigit())


def correct_name_lastname(txt):
    return "".join(w for w in txt if w.isalpha())


def is_all_alphabetic(txt):
    if not txt.isalpha():
        print(f"You entered '{txt}'. Please enter only alphabetic characters!")

    return txt


def encode_base64(txt):
    message_bytes = txt.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    print(base64_message)
    return base64_message

def simple_date_format(the_date):
    #print(the_date.strftime("%d.%m.%Y"))
    return the_date.strftime("%d.%m.%Y")


