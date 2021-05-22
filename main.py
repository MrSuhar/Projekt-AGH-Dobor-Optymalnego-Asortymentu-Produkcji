import PySimpleGUI as GUI
if __name__=="__main__":


    GUI.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[GUI.Button('boil'), GUI.Button('Exit')]]

    # Create the Window
    window = GUI.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == GUI.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
            break
        if event =='boil':
            print("Welcome to BOiL")

    window.close()



class Info:
    ilosc_srodkow_produkcji = 0
    ograniczenia_ilosci_srodkow_produkcji = 0

class Produkt:
    ilosc_srodkow_produkcji_na_wyrob = 0
    zyski_jednostkowe = 0
    ograniczenia_ilosci_poszczegolnych_wyrobow = 0

