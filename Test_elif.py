__author__ = 'Norbert'
print('Podaj swoje imie: ')
name = input()
print("podaj swoj wiek ")
age = input()
if name == 'Alice':
    print('Hi, Alice.')
elif int(age) < 12:
    print('You are not Alice, kiddo.')
elif int(age) > 100:
    print('You are not Alice, grannie.')
elif int(age) > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')