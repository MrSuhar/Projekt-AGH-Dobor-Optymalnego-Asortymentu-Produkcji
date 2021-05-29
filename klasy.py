from scipy.optimize import linprog
import numpy as np
class Info:
    ilosc_srodkow_produkcji = 0
    ograniczenia_ilosci_srodkow_produkcji = 0


class Produkt:
    ilosc_srodkow_produkcji_na_wyrob = []
    zyski_jednostkowe = 0
    ograniczenia_ilosci_poszczegolnych_wyrobow = 0


def optymalizuj(zyski, czas_pracy, limit_pieca, ograniczenia):
    print("Zyski : " + zyski)
    print("Czas pracy: " + czas_pracy)
    print("Limit pracy pieca h/1szt odlewu: " + limit_pieca)
    print("Ograniczenia : " + ograniczenia)

    srodki_produkcji = []
    zysk_calkowity = 0

    wynik = linprog(c=zyski, A_ub=czas_pracy, b_ub=limit_pieca, bounds=ograniczenia, method="simplex")

    # linprog.x -The independent variable vector which optimizes the linear programming problem.
    if wynik.success:
        wynik.x = list(map(lambda x: round(x, 0), wynik.x))

        ilosc_wyrobow = wynik.x
        zyski = zyski * (-1.0)

        for row in czas_pracy:
            srodki_produkcji.append(sum(wynik.x * row))

        zysk_calkowity = (wynik.fun * (-1))

        return ilosc_wyrobow, srodki_produkcji, zysk_calkowity
