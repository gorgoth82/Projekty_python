__author__ = 'nbaran'
catNames = []
while True:
    print('Wpisz imie kota'+str(len(catNames)+1)+
          ' (lub nacisnij enter aby zakonczyc)')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('Imiona kotow: ')
for name in catNames:
    print(' '+ name)