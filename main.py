# Написати валідації за допомогою регулярних виразів:
# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
# - домашній номер телефону (тільки цифри та довжина номера)
# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)


import re


#   Первое и второе задание поместил в 1 функцию
# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
# - домашній номер телефону (тільки цифри та довжина номера)

def is_tele(maybe_a_tele):
    for val in maybe_a_tele:
        if re.match(r"^0\d", val) and len(val) == 10:
            print(val, "is a phone number")
        elif re.match(r"^\+[380]\d", val) and len(val) == 13:
            print(val, "is a phone number")
        elif re.match(r"^[380]\d", val) and len(val) == 12:
            print(val, "is a phone number")
        elif re.match(r"^[1-9]\d", val) and len(val) == 7:
            print(val, "is a local phone number")
        else:
            print(val, "is NOT a phone number")

# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
def is_mail(maybe_a_email):
    for val in maybe_a_email:
        if re.match(r"^.{2,10}@gmail.com$", val):
            print(val, "is an email")
        else:
            print(val, "is NOT an email")


# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)

def is_fio(maybe_a_fio):
    for val in maybe_a_fio:
       if re.match(r"^[a-zA-Z]{2,20}\s[a-zA-Z]{2,20}\s[a-zA-Z]{2,20}$", val):
           print(val, "is a FIO")
       else:
           print(val, "is NOT a FIO")

try:

    maybe_phone = ["+38050112233", "+380671112233", "0671112233", "1234567891234", "1204567", "0000000"]
    maybe_email = ["@asd.net", "aaaa_123@gmail.com", "3@gmail.com"]
    maybe_fio = ["abc abc abc", "abC aBc Abc", "a abc abc", "555 abc abc", "abc abc ccccccccccccccccccccc"]
    is_tele(maybe_phone)
    is_mail(maybe_email)
    is_fio(maybe_fio)

except Exception as e:
    print(e)
