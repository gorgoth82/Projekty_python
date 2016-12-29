__author__ = 'nbaran'
#gra w zgadywanie liczby
import random
losowaLiczba = random.randint(1,20)

print('Podaj jak liczbe z przedzialu 1 do 20 mam na mysli. Masz 6 prob')
licznik = 1

for iloscRazy in range(1,6):
    print(str(licznik) + ' proba')
    licznik += 1
    try:
        odpowiedz = int(input())
    except ValueError:
        print('Nieprawidlowa wartosc')
        continue
    if odpowiedz > 20:
        print('Liczba z po za zakresu')
    elif losowaLiczba < odpowiedz:
        print('Mysle mniejszej liczbie')
    elif losowaLiczba > odpowiedz:
        print('Mysle o wiekszej liczbie')
    else:
        break

if odpowiedz == losowaLiczba:
    print('Brawo!!')
else:
    print('Na mysli mialem liczbe: ' + str(losowaLiczba))



