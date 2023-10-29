"""
By Michał Matuszyk
on 29/10/2023
"""
import WielomianyHelpers


def oblicz_wart_pochodnej_wielomianu_metoda_Hornera(wielomian, x):
    """
    :param wielomian: lista n elem. [a0, a1, a2, ..., an], gdzie
    W(x) = a0 + a1x + a1x^2 + ... + anx^n
    :param x: liczba
    :return: pochodna f
    """
    n = len(wielomian)
    p = wielomian[n - 1] * (n - 1)  # Ostatni wspolczynnik obliczamy
    for i in range(n - 1, 1, -1):
        k = i - 1  # bo liczymy od 0 ;)
        p = x * p + k * wielomian[k]
    return p


if __name__ == "__main__":
    przykladowy_wielomian = [1, 2, 3, 3]  # W(x) = 1 + x + x^2
    przykladowy_x = 1
    print("W(" + str(przykladowy_x) + ")=" + WielomianyHelpers.listaWielomianJakoStr(przykladowy_wielomian) + " =",
          oblicz_wart_pochodnej_wielomianu_metoda_Hornera(przykladowy_wielomian, przykladowy_x))
