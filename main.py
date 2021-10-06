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
        assert get_largest_prime_below(100) == 97
        assert get_largest_prime_below(17) == 17
        assert get_largest_prime_below(23) == 23


def get_age_in_days(birthday):
    data_nasterii_str_lst = birthday.split('/')
    data_nasterii_int_lst = []
    for fiecare_data in data_nasterii_str_lst:
        data_nasterii_int_lst.append(int(fiecare_data))
    return (2021-data_nasterii_int_lst[2]) * 365 + (data_nasterii_int_lst[1] - 10) * 30 + data_nasterii_int_lst[0] - 1


def test_get_age_in_days():
    assert get_age_in_days('07/03/2002') == 6731
    assert get_age_in_days('07/04/1999') == 7856
    assert get_age_in_days('30/11/200') == 664724



def get_goldbach(n):
    if n%2 == 1:
        return None
    else:
        if n==4:
            return 2,2
        p1=3
        p2=n-3
        while p1<p2:
            if(is_prime(p2)== True):
                return p1,p2
            p1+=2
            p2-=2


def test_get_goldbach():
    assert get_goldbach(100)== (3,97)
    assert get_goldbach(14) == (3,11)
    assert get_goldbach(16) == (3,13)
    assert get_goldbach(12) == (5,7)
    assert get_goldbach(4) == (2,2)


def main():
    print("1. Ultimul număr prim mai mic decât un număr dat.")
    print("2. Determinarea varstei unei persoane in zile.")
    print("3. Determinarea numerelor prime p1 si p2 astfel incat n=p1+p2")
    print("x.")
    while True:
        optiune = input("Alege optiunea: ")
        if optiune == '1':
         nr1=int(input("Dati numarul aici:"))
         print(f"ultimul numar prim mai mic decat numarul dat este: {get_largest_prime_below(nr1)}")
        elif optiune == '2':
             bday=input("Dati data nasterii: ")
             print(f"Numarul de zile traite este: {get_age_in_days(bday)}")
        elif optiune == '3':
                nr2=int(input("Dati numarul n aici: "))
                print(f"Cele 2 numere prime sunt: {get_goldbach(nr2)}")
        elif optiune == 'x':
             break

test_get_goldbach()
test_get_age_in_days()
test_get_largest_prime_below()
main()

