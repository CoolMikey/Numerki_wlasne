"""
By Michał Matuszyk
on 28/10/2023
"""


def oblicz_wart_wielomianu_metoda_Hornera(wielomian, x):
    """
    :param wielomian: lista n elem. [a0, a1, a2, ..., an], gdzie
    W(x) = a0 + a1x + a1x^2 + ... + anx^n
    :param x: liczba 
    :return: liczba
    """
    w = wielomian[len(wielomian) - 1]
    for ak in wielomian[:len(wielomian) - 1]:
        print("ak", ak)
        w = ak + x * w
    return w


if __name__ == "__main__":
    przykladowy_wielomian = [1, 1, 1]  # W(x) = 1 + x + x^2
    print("Wynik W(x) = 1 + x + x^2 W(1) to:", oblicz_wart_wielomianu_metoda_Hornera(przykladowy_wielomian, 1))
