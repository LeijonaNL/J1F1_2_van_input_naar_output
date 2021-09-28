# feestlunch2

prijs_croissant = 0.39
prijs_stokbrood = 2.78
aftrek_kortingsbon = -0.50


print('Prijs per croissant: ' + str(prijs_croissant))
aantal_croissant = int(input('Hoeveel croissants wilt U bestellen? '))
print('Aantal bestelde croissants: ' + str(aantal_croissant))

print('Prijs per stokbrood: ' + str(prijs_stokbrood))
aantal_stokbrood = int(input('Hoeveel stokbroden wilt U bestellen? '))
print('Aantal bestelde stokbroden: ' + str(aantal_stokbrood))

print('Aftrek per kortingsbon: ' + str(aftrek_kortingsbon))
aantal_kortingsbonnen = int(input('Hoeveel kortingsbonnen heeft U? '))
print('U heeft ' + str(aantal_kortingsbonnen) + ' kortingsbonnen ingevoerd')


totaalprijs_croissant = aantal_croissant * prijs_croissant
totaalprijs_stokbrood = aantal_stokbrood * prijs_stokbrood
totaalaftrek_korting = aantal_kortingsbonnen * aftrek_kortingsbon
eindprijs = totaalprijs_croissant + totaalprijs_stokbrood + totaalaftrek_korting

print('''  ----------------------------------------------------
   Product   Aantal   Totaal per product
|  Croissant '''  + str(aantal_croissant) + '''        ''' + str(totaalprijs_croissant) + '''
|  Stokbrood '''  + str(aantal_stokbrood) + '''        ''' + str(totaalprijs_stokbrood) + '''
|  Korting   '''    + str(aantal_kortingsbonnen) + '''        ''' + str(totaalaftrek_korting) + '''
---------------------------------------------------- 
|  Eindprijs = ''' + str(eindprijs) + '''
---------------------------------------------------- ''')