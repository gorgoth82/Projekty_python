__author__ = 'nbaran'
def collatz(number):
    if number % 2 == 0:
        print(str(number//2))
        return number//2
    else:
        print(str(3*number+1))
        return 3*number+1
wynik = 0
while wynik != 1:
    try:
        print('Podaj liczbe')
        userNumbert = int(input())
        wynik = collatz(userNumbert)
    except ValueError:
        print("Podales zla wartosc")

print('Wynik 1 konczy program')