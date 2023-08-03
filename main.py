# Написати валідації за допомогою регулярних виразів:
# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
# - домашній номер телефону (тільки цифри та довжина номера)
# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)

# or re.match(r'^+\d', val) and len(val) == 13
import re


#   Первое и второе задание поместил в 1 функцию
# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
# - домашній номер телефону (тільки цифри та довжина номера)

def is_tele(maybe_a_tele):
    for val in maybe_a_tele:
        if re.match(r"^0\d", val) and len(val) == 10:
            print(val, "is a phone number")
        elif re.match(r"^\+[380]\d", val) and len(val) == 12:
            print(val, "is a phone number")
        elif re.match(r"[1-9]\d", val) and len(val) == 7:
            print(val, "is a local phone number")
        else:
            print(val, "is NOT a phone number")





try:

    maybe_t_num = ["+38050112233", "+380671112233", "0441234567", "0671112233", "1234567891234", "1204567"]

    is_tele(maybe_t_num)

except Exception as e:
    print(e)
