import random

liczby = []
pocz_licznik = int(input('Poczaj poczatek zakresu '))
licznik = int(input('Podaj koniec zakresu '))

# Wypelnienie listy liczbami od 1 do 60"
while int(licznik) >= int(pocz_licznik):
    liczby.insert(licznik, licznik)
    licznik -= 1

# inicalizacja podstawowego generatora liczb losowych
random.seed()

# wylosowanie 6 liczby i wydrukowanie ich na ekran
print(random.sample(liczby, 6))

f = open('liczby.txt', 'w')
f.write(str(random.sample(liczby, 6)))
f.close()

