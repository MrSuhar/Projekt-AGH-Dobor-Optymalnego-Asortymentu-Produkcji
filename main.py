import PySimpleGUI as GUI
import numpy as np
import klasy
if __name__=="__main__":

    #TEST:
    zyski = np.array([1800., 2400., 3000.])
    czas_pracy = np.array([[5., 3., 1.], [1., 2., 4.]])
    limit_pieca = np.array([36000., 48000.])
    ograniczenia = [(0.0, 200.0), (0.0, 120.0), (0.0, 60.0)]

    #działa -----> PRZYKŁAD: http://delibra.bg.polsl.pl/Content/29220/BCPS_32889_-_Optymalny-dobor-asor_0000.pdf
    print(klasy.optymalizuj(zyski * (-1.0), czas_pracy, limit_pieca, ograniczenia))
    #do okreslenia czy program ma dalej dzialac
    flag=True

    #OKRESLENIE ILOSCI RODZAJOW SRODKOW PRODUKCJI
    ilosc_rodzajow_srodkow_produkcji=0

    GUI.theme('DarkAmber')
    #zawartosc okna
    layout = [[GUI.InputText(),GUI.Button('Dodaj ilosc rodzajow materialow')], [GUI.Button('Exit')]]

    #tworzenie okna
    window = GUI.Window('Ilosc rodzajow materialow', layout)

    while True:
        event, values = window.read()
        if event == GUI.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
            flag=False
            break
        if event =='Dodaj ilosc rodzajow materialow':

            if values[0]!='' and int(values[0])>0:
                ilosc_rodzajow_srodkow_produkcji=int(values[0])
                break
            else:
                continue
    window.close()

    # print(ilosc_rodzajow_srodkow_produkcji)

    # OKRESLENIE ILOSCI RODZAJOW PRODUKTOW
    ilosc_rodzajow_produktow = 0
    if flag:
        layout = [[GUI.InputText(),GUI.Button('Dodaj ilosc rodzajow produktow')], [GUI.Button('Exit')]]

        window = GUI.Window('Ilosc rodzajow produktow', layout)
        while True:
            event, values = window.read()
            if event == GUI.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
                flag=False
                break
            if event == 'Dodaj ilosc rodzajow produktow':
                if values[0] != '' and int(values[0]) > 0:
                    ilosc_rodzajow_produktow = int(values[0])
                    break
                else:
                    continue
        window.close()

    #print(ilosc_rodzajow_produktow)


    #DODAWANIE ILOSCI MATERIALOW POTRZEBNYCH DO WYPRODUKOWANIA KONKRETNEGO PRODUKTU

    #WORK IN PROGRESS-> dodac petle przechodzaca przez wszystkie produkty
    testowy_produkt=klasy.Produkt()
    if flag:
        nr_produktu='test'
        layout = [[GUI.Text('Zysk jednostkowy: '),GUI.InputText()],
                  [GUI.Text('Ograniczenie ilosci: '),GUI.InputText()]
            ,*[[GUI.Text("Srodek produkcji nr "+str(i+1)),GUI.InputText(), ] for i in range(ilosc_rodzajow_srodkow_produkcji)],
                   [GUI.Button('Zapisz'),GUI.Button('Exit')]]

        window=GUI.Window('Produkt '+str(nr_produktu), layout)
        while True:
            event, values = window.read()
            if event == GUI.WIN_CLOSED or event == 'Exit':
                flag=False
                break
            if event == 'Zapisz':
                #Dodawanie zyskow jednostkowych && ograniczenia ilosci
                if values[0] != '':
                    testowy_produkt.zyski_jednostkowe=int(values[0])
                if values[1] != '' and int(values[1])>=0:
                    testowy_produkt.ograniczenia_ilosci_poszczegolnych_wyrobow=int(values[1])

                #Dodawanie ilosci srodkow produkcji potrzebnych do wyproukowania 1 szt. danego wyrobu
                for i in range(len(values)):
                    #print(values[i])
                    if i>1:
                        if values[i]!='' and int(values[i])>=0:
                            testowy_produkt.ilosc_srodkow_produkcji_na_wyrob.append(int(values[i]))
        window.close()

        print("Zyski: "+ str(testowy_produkt.zyski_jednostkowe))
        print("Ograniczenie ilosci: " + str(testowy_produkt.ograniczenia_ilosci_poszczegolnych_wyrobow))
        print("Ilosc materialow na wyrob: " + str(testowy_produkt.ilosc_srodkow_produkcji_na_wyrob))








    #mana=klasy.Info()
    #mana.ilosc_srodkow_produkcji=11
    #print(mana.ilosc_srodkow_produkcji)


