import PySimpleGUI as GUI
import numpy as np
import klasy

if __name__ == "__main__":

   ####################################################################################################################

    # do okreslenia czy program ma dalej dzialac
    flag = True
    GUI.theme('DarkAmber')

     # OKRESLENIE ILOSCI RODZAJOW PRODUKTOW I ILOSCI SRODKOW PRODUKCJI
    ilosc_rodzajow_produktow = 0
    ilosc_rodzajow_srodkow_produkcji = 0
    if flag:
        layout = [[GUI.Text('Dodaj ilosc rodzajow wyrobow'),GUI.InputText()],[GUI.Text('Dodaj ilosc srodkow produkcji'),GUI.InputText()],[GUI.Button('Zapisz'),GUI.Button('Exit')]]

        window = GUI.Window('Ilosc rodzajow wyrobow i srodkow produkcji', layout)
        while True:
            event, values = window.read()
            if event == GUI.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
                flag = False
                break
            if event == 'Zapisz':
                if values[0] != '' and int(values[0]) > 0 and values[1] != '' and int(values[1]) > 0:
                    ilosc_rodzajow_produktow = int(values[0])
                    ilosc_rodzajow_srodkow_produkcji=int(values[1])
                    break
                else:
                    continue
        window.close()



    #OKRESLENIE PARAMETROW PRODOKTOW 
    zyski_jednostkowe=[]
    ograniczenia_ilosci_wyrobow=[]

    if flag:
        layout = [*[[GUI.Text("Wyrob " + str(i + 1)),GUI.Text("Zysk_jednostkowy: "),GUI.InputText(),GUI.Text("Ograniczenia: "),GUI.InputText(),GUI.InputText() ] for i in
                    range(ilosc_rodzajow_produktow)],
                      [GUI.Button('Zapisz'), GUI.Button('Exit')]]

        window = GUI.Window('Ilosc rodzajow wyrobow', layout)              
        while True:
            event, values = window.read()
            if event == GUI.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
                flag = False
                break
            if event == 'Zapisz':
                for i in range(len(values)):
                    if values[i] != '' and int(values[i]) >= 0:
                        if i % 3 ==0:
                            zyski_jednostkowe.append(int(values[i]))
                        if i %3==1:
                            if values[i+1] != '' and int(values[i+1]) >= 0:
                                tuple1=(int(values[i]),int(values[i+1]))
                                ograniczenia_ilosci_wyrobow.append(tuple1)
                            else:
                                tuple1=(int(values[i]),0)
                                ograniczenia_ilosci_wyrobow.append(tuple1)                                        
                break            
                        
        window.close()                 

    #OKRESLENIE PARAMETROW SRODKOW PRODUKCJI 
        limit_srodkow_produkcji=[]
        ilosc_zuzycia_srodka_produkcji=[]

        for i in range(ilosc_rodzajow_srodkow_produkcji):
            if flag:
                layout = [[GUI.Text("Srodek produkcji "+str(i+1))],*[[GUI.Text("Srodki produkcji na wyrob "+str(j+1)),GUI.InputText()]for j in range(ilosc_rodzajow_produktow)],[GUI.Text("Ogranicznie srodka produkcji:" ),GUI.InputText()],[GUI.Button('Zapisz'), GUI.Button('Exit')]]

                window = GUI.Window('Parametry srodkow produkcji', layout)              
                while True:
                    event, values = window.read()
                    if event == GUI.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
                        flag = False
                        break
                    if event == 'Zapisz':
                        tmp=[]
                        for k in range(len(values)):
                                if k<ilosc_rodzajow_produktow:
                                    tmp.append(int(values[k]))
                                else:
                                    ilosc_zuzycia_srodka_produkcji.append(tmp)
                                    limit_srodkow_produkcji.append(int(values[k]))                                            
                        break                
                                
                window.close()      
        
        zyski=np.array(zyski_jednostkowe)
        czas_pracy=np.array(ilosc_zuzycia_srodka_produkcji)
        limit_pieca=np.array(limit_srodkow_produkcji)
        ograniczenia=np.array(ograniczenia_ilosci_wyrobow)        
        wynik = klasy.optymalizuj(zyski, czas_pracy, limit_pieca, ograniczenia)

    #PREZENTACJA WYNIKOW
        if flag:
            layout = [
            *[[GUI.Text("Wyrob "+str(i+1)+": "+str(wynik.ograniczenia_ilosci_srodkow_produkcji[i]))]for i in range(ilosc_rodzajow_srodkow_produkcji)],
            [GUI.Text("Przychod calkowity: "+str(wynik.zysk_calkowity))],
            *[[GUI.Text("Srodek produkcji "+str(j+1)+": "+str(wynik.ilosc_srodkow_produkcji[j]))]for j in range(ilosc_rodzajow_srodkow_produkcji)],
            [GUI.Button('Exit')]]

            window = GUI.Window('Wyniki', layout)              
            while True:
                event, values = window.read()
                if event == GUI.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
                    flag = False
                    break            
                            
            window.close()

        #print(wynik.zysk_calkowity)
        #print(wynik.ograniczenia_ilosci_srodkow_produkcji) #finalny wynik
        #print(wynik.ilosc_srodkow_produkcji)

    # mana=klasy.Info()
    # mana.ilosc_srodkow_produkcji=11
    # print(mana.ilosc_srodkow_produkcji)
