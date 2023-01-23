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




