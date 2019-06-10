from tkinter import *
from gra import Pytania

okno = Tk()
okno.title("Milionerzy")
okno.geometry("960x640")
def naciskasz_a():
    Pytania.odpowiedz_użytkownika= 'twoja odpowiedź to a'
def naciskasz_b():
    Pytania.odpowiedz_użytkownika= 'twoja odpowiedź to b'
def naciskasz_c():
    Pytania.odpowiedz_użytkownika= 'twoja odpowiedź to c'
def naciskasz_d():
    Pytania.odpowiedz_użytkownika= 'twoja odpowiedź to d'
odp_a=Button(okno, text="A), self.wyniki['a']", Command=naciskasz_a)
odp_b=Button(okno, text="B), self.wyniki['b']", Command=naciskasz_b)
odp_c=Button(okno, text="C), self.wyniki['c']", Command=naciskasz_c)
odp_d=Button(okno, text="D), self.wyniki['d']", Command=naciskasz_d)





okno.mainloop()
