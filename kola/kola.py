import random
uzycie= [] #### zmienna która zapisuje użyte koła

def fifty(pytanie):
    ####funkcja pozwala na użycie koła ratunkowego pół na pół w grze milionerzyself.
    #### Usuwa ona 2 losowo wybrane błędne odpowiedzi i wyświetla jedną błędną i jedną prawidłową ułatwiając wybór graczowiself.
    #### abcd to kolejne odpowiedzi w danym pytaniu
    print('Skorzystałeś z koła pół na pół, oto pozostałe odpowiedzi')
    temp=random.randrange(1,3)
    if a==correct:
        temp_b=1
        temp_c=2
        temp_d=3
        if temp == temp_b:
            print(a, b)
        elif temp == temp_c:
            print(a, c)
        elif temp==temp_d:
            print(a,d)
def kola(odpowiedzi):
    #### funkcja pozwala wyśwetlić koła ratunkowe w grze milionerzy oraz skorzystać z nich
    while True:
        print('Jeśli chcesz skrorzystać z kołą ratunkowego wpisz koło')
        mozliwosc_kola = input()
        if mozliwosc_kola == koło:
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
                        fifty(pytanie[])
                        break
                    elif wybor == 2:
                        uzycie.append('tele')
                        telefon(pytanie[])
                        break
                    elif wybor ==3:
                        uzycie.append('publika')
                        przyjaciel(pytanie[])
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
                            telefon(pytanie[])
                            break
                        elif wybor ==3:
                            uzycie.append('publika')
                            przyjaciel(pytanie[])
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
                            fifty(pytanie[])
                            break
                        elif wybor ==3:
                            uzycie.append('publika')
                            przyjaciel(pytanie[])
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
                            fifty(pytanie[])
                            break
                        elif wybor == 2:
                            uzycie.append('tele')
                            telefon(pytanie[])
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
                                przyjaciel(pytanie[])
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
                                telefon(pytanie[])
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
                                fifty(pytanie[])
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
                                telefon(pytanie[])
                                break
                            elif wybor == 4:
                                print('wracamy do gry')
                                break
                elif len(uzycie)==3:
                    print('nie masz już kół')
                    break
