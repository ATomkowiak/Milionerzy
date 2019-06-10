import random
import os
import time
import colorama
import sys
import pyfiglet
from tkinter import *
import  termcolor
#NAPRAW KTOS TEN JEBANY BLAD ZE NIE DZIALA CALY PROGRAM
screen = Tk()
screen.geometry("230x298")
screen.resizable(0, 0)
screen.title("Milionerzy")
large_font = ('Verdana', 15)

x = 230
y = 300
e_y = 64
screen.y = BooleanVar()
button_x = (x/4)
button_y = ((y - e_y)/5)

class Pytania:
    def __init__(self):
        self.wyniki = {} #lista wynikow w ktorej sa odpowiedzi slowne
        self.wyniki1 = {} #lista wynikow w ktorej sa wartosci liczbowe (0 jest zawsze poprawne)
        self.abcd = ["a", "b", "c", "d"] #literki przy pytaniach
        self.hajs = 0
        self.znacznik = None
        #baza pytan i odpowiedzi
        self.pytania05 = ["Zwarta grupa zawodników jadących w wyścigu kolarskim to:",
                           "Który z wymienionych pojazdów nie jest wyposażony w gąsienice:",
                           "Mężczyzna zabiegający o względy kobiety to:",
                           "Który z wymienionych ptaków nie potrafi latać ?",
                           "Co Kopciuszek zgubił na schodach pałacu ?", ]

        self.odpowiedzi05 = [["peleton", "aktyw", "konwój", "plejada"],
                              ["autokar", "czołg", "ratrak", "koparka"],
                              ["adorator", "kombinator", "operator", "administrator"],
                              ["strus", "orzeł", "tukan", "albatros"],
                              ["pantofelek", "chusteczkę", "parasolkę", "torebkę"]]

        self.pytania1 = ["Ile prac musiał wykonać Herakles w służbie u Eurysteusza ?",
                            "Zamiar wyprzedzania (względnie: omijania) w pojeździe mechanicznym sygnalizowany jest:",
                            "Do jakiego gatunku należą filmy pt. „Amityville”, „Halloween”, czy „Koszmar z ulicy Wiązów” ?",
                            "Kreon skazał Antygonę na:",
                            "Kształt jakiej litery ma bramka w rugby ?"]

        self.odpowiedzi1 = [["12", "5", "9", "20"],
                               ["kierunkowskazem", "światłem stopu", "światłami postojowymi", "krótkim postojowym"],
                               ["do horroru", "do komedii", "do melodramatu", "do westernu"],
                               ["zamurowanie żywcem", "ścięcie", "powieszenie", "uduszenie"],
                               ["H", "U", "Y", "T"]]

        self.pytania2 = ["Kopaliną nie jest:",
                            "Który z piłkarzy na mistrzostwach świasta w Meksyku w 1986 roku zdobył gola dzięki „ręce boskiej” ?",
                            "Jak nazywa się gruczoł wydzielający inulinę ?",
                            "Jaką roślinę nazywamy niekiedy słodkim ziemniakiem ?",
                            "Najmniejsza jednostka ilości informacji to:"]

        self.odpowiedzi2 = [["cement", "żwir", "glina", "margiel"],
                               ["Diego Maradona", "Gary Lineker", "Michel Platini", "Paolo Rossi"],
                               ["trzustka", "nadnercza", "tarczyca", "przysadka móżgowa"],
                               ["batat", "bambus", "jams", "burak"],
                               ["bit", "piksel", "octet", "bajt"]]

        self.pytania4 = ["Kiedy obchodzony jest Dzień Matki ?",
                            "„Iron man” to przebój grupy:",
                            "Zinedine Zidane to piłkarz grający w czasie finałów Mistrzostw Świata we Francji w 1998 roku w reprezentacji:",
                            "Do jakiego kraju należy Grenlandia ?",
                            "Tajemnica zabójstwa Laury Palmer jest jednym z głównych tematów serialu:"]

        self.odpowiedzi4 =[["26 maja", "21 stycznia", "8 marca", "23 czerwca"],
                              ["Black Sabbath", "Iron Maiden", "AC\DC", "Led Zeppelim"],
                              ["Francji", "Włoch", "Hiszlanii", "Brazylii"],
                              ["do Danii", "do Wielkiej Brytanii", "do USA", "do Szwecji"],
                              ["Twin Peaks", "Stranger Things", "Z Archiwum X", "Star Wars"]]

        self.pytania8 = ["Kto sformułował prawo powszechnego ciążenia ?",
                            "Jaką kolonię uważano za „klejnot w koronie” brytyjskiego imperium ?",
                            "Jak nazywał się czarodziej z trylogii J.R.R. Tolkiena pt. „Władca Pierścieni” ?",
                            "Estry to pochodne:",
                            "Jak nazywał się książę trojański, zabity przez Achillesa ?"]

        self.odpowiedzi8 = [["Isaac Newton", "Albert Einstein", "Max Planck", "Michael Faraday"],
                               ["Indie", "Malaje", "Egipt", "Brimę"],
                               ["Gandalf", "Aragorn", "Boromir", "Legolas"],
                               ["kwasów i alkoholi", "kwasów i zasad", "alkoholi i soli", "zasad i soli"],
                               ["Hektor", "Patroklos", "Astyanaks",  "Priam"]]

        self.pytania16 = ["W hokeju na trawie drużyna razem z bramkarzem liczy:",
                          "Do dynastii Andegawenów należał:",
                          "Który z kątów nie jest płaski ?",
                          "Kto był prezydentem USA w momencie wybuchu wojny secesyjnej ?",
                          "Gniazdo którego z wymienionych ptaków przypomina rękawicę z jednym palcem ?"]

        self.odpowiedzi16 = [["11 zawodników", "9 zawodników", "10 zawodników", "12 zawodników"],
                             ["Ludwik Węgierski", "Leszek Czarny", "Henryk Walezy", "Henryk IV Probus"],

                             ["dwuścienny", "rozwarty", "skierowany", "pełny"],
                             ["Abraham Lincoln", "Greorge Washington", "Millard Fillmore", "William Henry Harrison"],
                             ["remiza", "zimorodka", "perkoza", "jemiołuszki"]]

        self.pytania32 = ["Gdzie rozegrano pierwsze mistrzostwa świata w piłce nożnej w 1930 roku ?",
                          "Jak długo „żyje” czerwona krwinka u człowieka ?",
                          "Meduzę zabił:"]

        self.odpowiedzi32 = [["w Urugwaju", "w Meksyku", "we Francji", "w Argentynie"],
                             ["około 120 dni", "około 30 dni", "około 250 dni", "około 360 dni"],
                             ["Perseusz", "Tezeusz", "Herakles", "Jazon"]]

        self.pytania64 = ["W którym wieku wielka epidemia dżumy zebrała żniwo trzydziestu procent ludności Europy ?",
                          "Jak nazywał się zakon utworzony w celu obrony pielgrzymów przybywających do Ziemi Świętej ?",
                          "Który z podróżników uważany jest za odkrywcę Australii ?"]

        self.odpowiedzi64 = [["w XIV", "w XIIV", "w XII", "w XV"],
                             ["templariuszy", "norbertanów", "bonifratrów", "jezuitów"],
                             ["James Cook", "Luis de Torres", "Ferdynand Magellan", "Krzysztof Kolumb"]]

        self.pytania125 = ["Który z bogów Egiptu został zabity przez Seta, rozerwany na kawałki i rozrzucony po świecie ?",
                           "Z którym z podanych krajów nie graniczy Finlandia ?",
                           "Która z wymienionych planet ma tyle samo księżyców co Ziemia ?"]

        self.odpowiedzi125 = [["Ozyrys", "Ptah", "Horus", "Anubis"],
                              ["z Łotwą", "z Norwegią", "ze Szwecją", "z Rosją"],
                              ["Pluton", "Merkury", "Jowisz", "Neptun"]]

        self.pytania250 = ["Ostatnią bitwą w kampanii wrześniowej była bitwa:",
                           "Ilu braci miał Robinson Crusoe, główny bohater powieści Daniela Defoe ?",
                           "Tył języka najsilniej reaguje na smak:"]

        self.odpowiedzi250 = [["pod Kockiem", "nad Bzurą", "pod Szackiem", "pod Tomaszowem"],
                              ["dwóch", "trzech", "czterech", "pięciu"],
                              ["gorzki", "słodki", "słony", "kwaśny"]]

        self.pytania500 = ["Dziesięciocyfrowy międzynarodowy znormalizowany numer książki to:",
                           "W konkursie jakiego tańca startują Mia Wallace i Vincent Vega w filmie pt. „Pulp Fiction” ?",
                           "Wybrany do Senatu może być obywatel polski, mający prawo wybierania, który najpóźniej w dniu wyborów skończy:"]

        self.odpowiedzi500 = [["ISBN", "ISSN", "ICBM", "IRBM"],
                              ["twista", "tanga", "mambo", "rumby"],
                              ["30 lat", "25 lat", "21 lat", "18 lat"]]

        self.pytania1000 = ["Po ilu latach drużyna Los Angeles Lakers w sezonie 1999/2000 znów wywalczyła tytuł mistrza NBA ?",
                            "Aktorką, która stała się pierwowzorem filmowego wampa była:"]

        self.odpowiedzi1000 = [["po 12", "po 5", "po 18", "po 9"],
                               ["Theda Bara", "Pola Negri", "Mae West", "Mary Pickford"]]
    def pytanie1(self, pytania, odpowiedzi, nagroda, ):
        self.pytanie = random.randint(0, len(pytania) - 1) #losowanie pytania
        self.o = [0, 1, 2, 3] #numery pytan, gdzie 0 jest zawsze poprawne

        for i in range(1, 5): #tworzenie i losowanie odpowiedzi
            self.los = random.choice(self.o)
            self.wyniki[str(self.abcd[i-1])] = str(odpowiedzi[self.pytanie] [self.los])
            self.wyniki1[str(self.abcd[i-1])] = self.los
            #print(self.wyniki1)
            #print(self.wyniki)
            self.o.remove(self.los) #usuwamy z listy numer odpowiedzi w celu braku powtorzen

        print("Pytanie za", nagroda, "zł to:") #wyswietlanie pytania
        time.sleep(1)
        print(pytania[self.pytanie])
        time.sleep(1)
        b1 = Button(screen, text=("A",self.wyniki['a']) , font=large_font, highlightbackground="black", fg="white")
        b1.place(height=button_y, width=button_x, x=0, y=e_y + button_y + button_y + button_y - 1)

        b2 = Button(screen, text=("B)", self.wyniki['b']), font=large_font, highlightbackground="black", fg="white")
        b2.place(height=button_y, width=button_x, x=button_x, y=e_y + button_y + button_y + button_y - 1)

        b3 = Button(screen, text=("C)", self.wyniki['c']), font=large_font, highlightbackground="black", fg="white")
        b3.place(height=button_y, width=button_x, x=button_x + button_x , y= 0)

        b4 = Button(screen, text=("D)" , self.wyniki['d']), font=large_font, highlightbackground="black", fg="white")
        b4.place(height=button_y, width=button_x, x=button_x + button_x + button_x,
                 y=e_y + button_y + button_y + button_y - 1)

        time.sleep(1)
        self.odpowiedz_użytkownika = str(input("Twoja odpowiedź to: "))

        # sprawdzenie czy dobra odpowiedz
        if self.wyniki1[self.odpowiedz_użytkownika] == 0:
            self.hajs = nagroda
            print("Brawo ziom, masz na koncie", self.hajs, "zł")
            self.znacznik = True
            time.sleep(3)
            os.system('clear')


        elif self.wyniki1[self.odpowiedz_użytkownika] == 1 or self.wyniki1[self.odpowiedz_użytkownika] == 2 or \
                self.wyniki1[self.odpowiedz_użytkownika] == 3:
            print("przejebałeś stary masz na koncie", self.hajs,"zł" )
            self.znacznik = False




class Menu:
    def __init__(self):
        self.ascii_bannera = ''
    def wyświetl(self):
        print("Wpisz 'play' aby zagrać")
        print("Kliknij 't' aby wyświetlić twórców ")
        print("Kliknij 'q' aby wyjść")

    def tworycy(self):
        self.ascii_bannera = pyfiglet.figlet_format("TWÓRCY")
        print(self.ascii_bannera)
        print("Robert Kozak")
        print("Antek Tomkowiak")
        print("Patryk Kamiński")

    def wyjście(self):
        sys.exit()


ascii_banner = pyfiglet.figlet_format("MILIONERZY")
print(ascii_banner)
menu = Menu()
menu.wyświetl()
ogor = input()
if ogor == 'play':
    os.system('clear')
    kupa = Pytania()
    kupa.pytanie1(kupa.pytania05, kupa.odpowiedzi05, 500)
    if kupa.znacznik == True:
        kupa.pytanie1(kupa.pytania1, kupa.odpowiedzi1, 1000)
        if kupa.znacznik == True:
            kupa.pytanie1(kupa.pytania2, kupa.odpowiedzi2, 2000)
            if kupa.znacznik == True:
                kupa.pytanie1(kupa.pytania4, kupa.odpowiedzi4, 4000)
                if kupa.znacznik == True:
                    kupa.pytanie1(kupa.pytania8, kupa.odpowiedzi8, 8000)
                    if kupa.znacznik == True:
                        kupa.pytanie1(kupa.pytania16, kupa.odpowiedzi16, 16000)
                        if kupa.znacznik == True:
                            kupa.pytanie1(kupa.pytania32, kupa.odpowiedzi32, 32000)
                            if kupa.znacznik == True:
                                kupa.pytanie1(kupa.pytania64, kupa.odpowiedzi64, 64000)
                                if kupa.znacznik == True:
                                    kupa.pytanie1(kupa.pytania125, kupa.odpowiedzi125, 125000)
                                    if kupa.znacznik == True:
                                        kupa.pytanie1(kupa.pytania250, kupa.odpowiedzi250, 250000)
                                        if kupa.znacznik == True:
                                            kupa.pytanie1(kupa.pytania500, kupa.odpowiedzi500, 500000)
                                            if kupa.znacznik == True:
                                                kupa.pytanie1(kupa.pytania1000, kupa.odpowiedzi1000, 1000000)
elif ogor == 't':
    menu.tworycy()

elif ogor == 'q':
    menu.wyjście()






screen.mainloop()