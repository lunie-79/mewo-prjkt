import random 
znaki = '1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*()-=[]\;QWERTYUIOPASDFGHJKLZXCVBNM'
wylosuj = int(input('Podaj długość hasła'))
haslo = ''
for i in range(wylosuj):
    r = random.randint(0,len(znaki)-1)
    haslo += znaki[r]
print(haslo)
