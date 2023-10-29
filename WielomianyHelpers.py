"""
By Michał Matuszyk
on 29/10/2023
"""


def listaWielomianJakoStr(wielomian):
    if len(wielomian) < 1:
        raise Exception("Wielomian nie może być pustą listą")
    if len(wielomian) == 1:
        return "0"
    str_wynikowy = str(wielomian[0])
    for i in range(1, len(wielomian)):
        if i > 0:
            if wielomian[i] != 0:
                if wielomian[i] == 1:
                    wielomian[i] = ""
                str_wynikowy = str_wynikowy + "+" + str(wielomian[i]) + "x^" + str(i + 1)

        else:
            str_wynikowy = str_wynikowy + "+" + str(wielomian[i]) + "x"
        print(i, str_wynikowy, wielomian[i])
    return str_wynikowy


if __name__ == "__main__":
    przykladowy_wielomian = [1, 0, 5, 4, 7, 0, 6]
    print(listaWielomianJakoStr(przykladowy_wielomian))
