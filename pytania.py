import random
import os
import time
import colorama
import  termcolor
class Pytania:
    def __init__(self):
        self.wyniki = {} #lista wynikow w ktorej sa odpowiedzi slowne
        self.wyniki1 = {} #lista wynikow w ktorej sa wartosci liczbowe (0 jest zawsze poprawne)
        self.abcd = ["a", "b", "c", "d"] #literki przy pytaniach
        self.hajs = 0
        self.znacznik = None
        #baza pytan i odpowiedzi
        self.pytania500 = ["Zwarta grupa zawodników jadących w wyścigu kolarskim to:",
                           "Który z wymienionych pojazdów nie jest wyposażony w gąsienice:",
                           "Mężczyzna zabiegający o względy kobiety to:",
                           "Który z wymienionych ptaków nie potrafi latać ?",
                           "Co Kopciuszek zgubił na schodach pałacu ?", ]

        self.odpowiedzi500 = [["peleton", "aktyw", "konwój", "plejada"],
                              ["autokar", "czołg", "ratrak", "koparka"],
                              ["adorator", "kombinator", "operator", "administrator"],
                              ["strus", "orzeł", "tukan", "albatros"],
                              ["pantofelek", "chusteczkę", "parasolkę", "torebkę"]]

        self.pytania1000 = ["Ile prac musiał wykonać Herakles w służbie u Eurysteusza ?",
                            "Zamiar wyprzedzania (względnie: omijania) w pojeździe mechanicznym sygnalizowany jest:",
                            "Do jakiego gatunku należą filmy pt. „Amityville”, „Halloween”, czy „Koszmar z ulicy Wiązów” ?",
                            "Kreon skazał Antygonę na:",
                            "Kształt jakiej litery ma bramka w rugby ?"]

        self.odpowiedzi1000 = [["12", "5", "9", "20"],
                               ["kierunkowskazem", "światłem stopu", "światłami postojowymi", "krótkim postojowym"],
                               ["do horroru", "do komedii", "do melodramatu", "do westernu"],
                               ["zamurowanie żywcem", "ścięcie", "powieszenie", "uduszenie"],
                               ["H", "U", "Y", "T"]]

        self.pytania2000 = ["Kopaliną nie jest:",
                            "Który z piłkarzy na mistrzostwach świasta w Meksyku w 1986 roku zdobył gola dzięki „ręce boskiej” ?",
                            "Jak nazywa się gruczoł wydzielający inulinę ?",
                            "Jaką roślinę nazywamy niekiedy słodkim ziemniakiem ?",
                            "Najmniejsza jednostka ilości informacji to:"]

        self.odpowiedzi2000 = [["cement", "żwir", "glina", "margiel"],
                               ["Diego Maradona", "Gary Lineker", "Michel Platini", "Paolo Rossi"],
                               ["trzustka", "nadnercza", "tarczyca", "przysadka móżgowa"],
                               ["batat", "bambus", "jams", "burak"],
                               ["bit", "piksel", "octet", "bajt"]]

        self.pytania4000 = ["Kiedy obchodzony jest Dzień Matki ?",
                            "„Iron man” to przebój grupy:",
                            "Zinedine Zidane to piłkarz grający w czasie finałów Mistrzostw Świata we Francji w 1998 roku w reprezentacji:",
                            "Do jakiego kraju należy Grenlandia ?",
                            "Tajemnica zabójstwa Laury Palmer jest jednym z głównych tematów serialu:"]

        self.odpowiedzi4000 =[["26 maja", "21 stycznia", "8 marca", "23 czerwca"],
                              ["Black Sabbath", "Iron Maiden", "AC\DC", "Led Zeppelim"],
                              ["Francji", "Włoch", "Hiszlanii", "Brazylii"],
                              ["do Danii", "do Wielkiej Brytanii", "do USA", "do Szwecji"],
                              ["Twin Peaks", "Stranger Things", "Z Archiwum X", "Star Wars"]]

        self.pytania8000 = ["Kto sformułował prawo powszechnego ciążenia ?",
                            "Jaką kolonię uważano za „klejnot w koronie” brytyjskiego imperium ?",
                            "Jak nazywał się czarodziej z trylogii J.R.R. Tolkiena pt. „Władca Pierścieni” ?",
                            "Estry to pochodne:",
                            "Jak nazywał się książę trojański, zabity przez Achillesa ?"]

        self.odpowiedzi8000 = [["Isaac Newton", "Albert Einstein", "Max Planck", "Michael Faraday"],
                               ["Indie", "Malaje", "Egipt", "Brimę"],
                               ["Gandalf", "Aragorn", "Boromir", "Legolas"],
                               ["kwasów i alkoholi", "kwasów i zasad", "alkoholi i soli", "zasad i soli"],
                               ["Hektor", "Patroklos", "Astyanaks",  "Priam"]]


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
        print("A)", self.wyniki['a'], "B)", self.wyniki['b'])
        time.sleep(1)
        print("C)", self.wyniki['c'],"D)" , self.wyniki['d'])
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




kupa = Pytania()
kupa.pytanie1(kupa.pytania500, kupa.odpowiedzi500, 500)
if kupa.znacznik == True:
    kupa.pytanie1(kupa.pytania1000, kupa.odpowiedzi1000, 1000)
    if kupa.znacznik == True:
        kupa.pytanie1(kupa.pytania2000, kupa.odpowiedzi2000, 2000)
        if kupa.znacznik == True:
            kupa.pytanie1(kupa.pytania4000, kupa.odpowiedzi4000, 4000)
            if kupa.znacznik == True:
                kupa.pytanie1(kupa.pytania8000, kupa.odpowiedzi8000, 8000)


