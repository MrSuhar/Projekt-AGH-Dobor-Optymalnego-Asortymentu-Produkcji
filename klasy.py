from scipy.optimize import linprog
import numpy as np

class Info:
    ilosc_srodkow_produkcji = 0
    ograniczenia_ilosci_srodkow_produkcji = 0
    zysk_calkowity = 0


class Produkt:    
    zyski_jednostkowe = 0
    ograniczenia=0

#class Srodek_Produkcji:



def optymalizuj(zyski, czas_pracy, limit_pieca, ograniczenia):

    print("Wczytano:")
    print("Zyski: \t", zyski)
    print("Czas pracy: \t",czas_pracy)
    print("Limit pracy pieca: \t ",limit_pieca)
    print("Ograniczenia: \t",ograniczenia)
    print("----------------------------")

    zyski = zyski * (-1.0)
    srodki_produkcji = []
    zysk_calkowity = 0

    # linprog.x -The independent variable vector which optimizes the linear programming problem.
    try:
        wynik = linprog(c=zyski,
                        A_ub=czas_pracy,
                        b_ub=limit_pieca,
                        bounds=ograniczenia,
                        method="simplex")

        if wynik.success:
            wynik.x = list(map(lambda x: round(x, 0), wynik.x))

            ilosc_wyrobow = wynik.x
            zyski = zyski * (-1.0)

            for row in czas_pracy:
                srodki_produkcji.append(sum(wynik.x * row))

            zysk_calkowity = (wynik.fun * (-1))

            info = Info()
            info.ilosc_srodkow_produkcji = srodki_produkcji
            info.ograniczenia_ilosci_srodkow_produkcji = ilosc_wyrobow
            info.zysk_calkowity = zysk_calkowity

            return info
    except:
        print("Nie można zoptymalizować")
        return 1
