def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3,x//2,2):
            if x%i==0:
                return False
    return True

def get_largest_prime_below(n):
    for i in range(n,1,-1):
        if is_prime(i):
            return i
def test_get_largest_prime_below():
    while True:
        if get_largest_prime_below(100) == 97:
            pass
        if get_largest_prime_below(17) == 17:
            pass
        if get_largest_prime_below(23) == 23:
            pass




def get_age_in_days(birthday):
    data_nasterii_str_lst = birthday.split('/')
    data_nasterii_int_lst = []
    for fiecare_data in data_nasterii_str_lst:
        data_nasterii_int_lst.append(int(fiecare_data))
    return (2021-data_nasterii_int_lst[2]) * 365 + (data_nasterii_int_lst[1] - 10) * 30 + data_nasterii_int_lst[0] - 1
def test_get_age_in_days():
    if get_age_in_days('07/03/2002')==6731:
        pass
    if get_age_in_days('07/04/1999')==7856:
        pass
    if get_age_in_days('30/11/200')== 664724:
        pass

def main():
    print("1. Ultimul număr prim mai mic decât un număr dat.")
    print("2. Determinarea varstei unei persoane in zile.")
    print("x.")
    while True:
        optiune = input("Alege optiunea: ")
        if optiune == '1':
         nr1=int(input("Dati numarul aici:"))
         print(f"ultimul numar prim mai mic decat numarul dat este: {get_largest_prime_below(nr1)}")
        elif optiune == '2':
             bday=input("Dati data nasterii: ")
             print(f"Numarul de zile traite este: {get_age_in_days(bday)}")
        elif optiune == 'x':
             break

main()
test_get_age_in_days()
test_get_largest_prime_below()
