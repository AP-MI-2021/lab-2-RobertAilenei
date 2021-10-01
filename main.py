'''get_largest_prime_below(n):'''


def get_age_in_days(birthday):
    data_nasterii_str_lst = birthday.split('/')
    data_nasterii_int_lst = []
    for fiecare_data in data_nasterii_str_lst:
        data_nasterii_int_lst.append(int(fiecare_data))
    return (2021-data_nasterii_int_lst[2]) * 365 + (data_nasterii_int_lst[1] - 10) * 30 + data_nasterii_int_lst[0] - 1



def main():
    print("1. Ultimul număr prim mai mic decât un număr dat.")
    print("2. Determinarea varstei unei persoane in zile.")
    print("x.")
    optiune = input("Alege optiunea: ")
    if optiune == '2':
        bday=input("Dati data nasterii: ")
        print(get_age_in_days(bday))


main()