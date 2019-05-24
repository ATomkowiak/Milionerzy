import random
import time
uzycie= [] #### zmienna która zapisuje użyte koła

def fifty(Pytania):
    ####funkcja pozwala na użycie koła ratunkowego pół na pół w grze milionerzyself.
    #### Usuwa ona 2 losowo wybrane błędne odpowiedzi i wyświetla jedną błędną i jedną prawidłową ułatwiając wybór graczowiself.
    #### abcd to kolejne odpowiedzi w danym pytaniu
    print('Skorzystałeś z koła pół na pół, oto pozostałe odpowiedzi')
    temp=random.randrange(1,3)
    while True:
        temp_b=1
        temp_c=2,
        temp_d=3
        if temp == temp_b:
            pytania.wyniki1.remove(2,3)
            print(Pytania.wyniki)
            break
        elif temp == temp_c:
            pytania.wyniki1.remove(1,3)
            print(Pytania.wyniki)
            break
        elif temp==temp_d:
            pytania.wyniki1.remove(1,2)
            print(Pytania.wyniki)
            break
def telefon(Pytania):
    #### funkcja zwraca prawdidłową odpowiedź z 75% poprawnością
    prop = random.random()
    while True:
        if prop>0.25:
            pytania.wyniki1.remove(1,2,3)
            print(Pytania.wyniki)
            break
        else:
            pytania.wyniki1.remove(0,1,2)
            print(Pytania.wyniki)
            break
def przyjaciel(Pytania):
        #### funkcja pozwala użyć koła pomoc od publicznośći i zwraca prawidłową odpowiedź z 60% poprawnością
        prawd=random.random()
        while True:
            if prawd>0.4:
                pytania.wyniki1.remove(1,2,3)
                print(Pytania.wyniki)
                break
            else:
                pytania.wyniki1.remove(0,1,2)
                print(Pytania.wyniki)
                break
def kola(Pytania):
    #### funkcja pozwala wyśwetlić koła ratunkowe w grze milionerzy oraz skorzystać z nich a także odejść ze zdobytą już kwotą
    while True:
        print('Jeśli chcesz skrorzystać z kołą ratunkowego wpisz koło')
        time.sleep(1)
        print('Jeśli chcesz odejść z kwotą gwarantowaną wpisz kwota')
        time.sleep(1)
        print('Jeśli chcesz grać dalej bez koła wpisz gram')
        mozliwosc_kola = input()
        if mozliwosc_kola == 'kwota':
            print("Gratulacje!")
            time.sleep(1)
            print("Wygrałeś", pytania.hajs, 'zł')
            menu.wyjście()
        elif mozliwosc_kola == 'koło':
            if len(uzycie)==0:
                while True:
                    print('Którego koła chcesz użyć?')
                    print('Jeśli chcesz skorzystać z pół na pół wciśnij 1')
                    print('Jeśli chcesz skrozystać z telefonu do przyjaciela wciśnij 2')
                    print('Jeśli chcesz skorzystać z pomocy publiczności wciśnij 3')
                    print('Jeśli nie chcesz korzystać z koła wciśnij 4')
                    wybor=int(input())
                    if wybor == 1:
                        uzycie.append('fifty')
                        fifty()
                        break
                    elif wybor == 2:
                        uzycie.append('tele')
                        telefon()
                        break
                    elif wybor ==3:
                        uzycie.append('publika')
                        przyjaciel()
                        break
                    elif wybor == 4:
                        print('wracamy do gry')
                        break
            elif len(uzycie)==1:
                if 'fifty' in uzycie:
                    while True:
                        print('Którego koła chcesz użyć?')
                        print('Jeśli chcesz skrozystać z telefonu do przyjaciela wciśnij 2')
                        print('Jeśli chcesz skorzystać z pomocy publiczności wciśnij 3')
                        print('Jeśli nie chcesz korzystać z koła wciśnij 4')
                        wybor=int(input())
                        if wybor == 2:
                            uzycie.append('tele')
                            telefon()
                            break
                        elif wybor ==3:
                            uzycie.append('publika')
                            przyjaciel()
                            break
                        elif wybor == 4:
                            print('wracamy do gry')
                            break
                elif 'tele' in uzycie:
                    while True:
                        print('Którego koła chcesz użyć?')
                        print('Jeśli chcesz skorzystać z pół na pół wciśnij 1')
                        print('Jeśli chcesz skorzystać z pomocy publiczności wciśnij 3')
                        print('Jeśli nie chcesz korzystać z koła wciśnij 4')
                        wybor=int(input())
                        if wybor == 1:
                            uzycie.append('fifty')
                            fifty()
                            break
                        elif wybor ==3:
                            uzycie.append('publika')
                            przyjaciel()
                            break
                        elif wybor == 4:
                            print('wracamy do gry')
                            break
                elif 'publika' in uzycie:
                    while True:
                        print('Którego koła chcesz użyć?')
                        print('Jeśli chcesz skorzystać z pół na pół wciśnij 1')
                        print('Jeśli chcesz skrozystać z telefonu do przyjaciela wciśnij 2')
                        print('Jeśli nie chcesz korzystać z koła wciśnij 4')
                        wybor=int(input())
                        if wybor == 1:
                            uzycie.append('fifty')
                            fifty()
                            break
                        elif wybor == 2:
                            uzycie.append('tele')
                            telefon()
                            break
                        elif wybor == 4:
                            print('wracamy do gry')
                            break
            elif len(uzycie)==2:
                if 'fifty' in uzycie:
                    if 'tele' in uzycie:
                        while True:
                            print('Którego koła chcesz użyć?')
                            print('Jeśli chcesz skorzystać z pomocy publiczności wciśnij 3')
                            print('Jeśli nie chcesz korzystać z koła wciśnij 4')
                            wybor=int(input())
                            if wybor ==3:
                                uzycie.append('publika')
                                przyjaciel()
                                break
                            elif wybor == 4:
                                print('wracamy do gry')
                                break
                    elif 'publika' in uzycie:
                        while True:
                            print('Którego koła chcesz użyć?')
                            print('Jeśli chcesz skrozystać z telefonu do przyjaciela wciśnij 2')
                            print('Jeśli nie chcesz korzystać z koła wciśnij 4')
                            wybor=int(input())
                            if wybor == 2:
                                uzycie.append('tele')
                                telefon()
                                break
                            elif wybor == 4:
                                print('wracamy do gry')
                                break
                elif 'publika' in uzycie:
                    if 'tele' in uzycie:
                        while True:
                            print('Którego koła chcesz użyć?')
                            print('Jeśli chcesz skorzystać z pół na pół wciśnij 1')
                            print('Jeśli nie chcesz korzystać z koła wciśnij 4')
                            wybor=int(input())
                            if wybor == 1:
                                uzycie.append('fifty')
                                fifty()
                                break
                            elif wybor == 4:
                                print('wracamy do gry')
                                break
                    elif 'fifty' in uzycie:
                        while True:
                            print('Którego koła chcesz użyć?')
                            print('Jeśli chcesz skrozystać z telefonu do przyjaciela wciśnij 2')
                            print('Jeśli nie chcesz korzystać z koła wciśnij 4')
                            wybor=int(input())
                            if wybor == 2:
                                uzycie.append('tele')
                                telefon(pytanie1.pytanie)
                                break
                            elif wybor == 4:
                                print('wracamy do gry')
                                break
                elif len(uzycie)==3:
                    print('nie masz już kół')
                    break
        elif mozliwosc_kola == 'gram':
            print('wracamy do gry')
            break
