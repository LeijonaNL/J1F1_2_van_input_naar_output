# Pizza calculator

prijs_Small = 1
prijs_Medium = 2
prijs_large = 3

print('Prijs per small: ' + str(prijs_Small))
aantal_Small = int(input('Hoeveel small pizzas wilt U bestellen? '))
print('U heeft ' + str(aantal_Small) + ' small pizzas geselecteerd.')

print('Prijs per medium: ' + str(prijs_Medium))
aantal_Medium = int(input('Hoeveel medium pizzas wilt U bestellen? '))
print('U heeft ' + str(aantal_Medium) + ' medium pizzas geselecteerd.')

print('Prijs per large: ' + str(prijs_large))
aantal_Large = int(input('Hoeveel large pizzas wilt U bestellen? '))
print('U heeft ' + str(aantal_Large) + ' large pizzas geselecteerd.')

totaalPrijs_Small = prijs_Small * aantal_Small
totaalPrijs_Medium = prijs_Medium * aantal_Medium
totaalPrijs_Large = prijs_large * aantal_Large
eindPrijs = totaalPrijs_Small + totaalPrijs_Medium + totaalPrijs_Large

print('''  ----------------------------------------------------
   Product       Aantal   Totaal per product
|  Small pizza   '''  + str(aantal_Small) + '''        ''' + str(totaalPrijs_Small) + '''
|  Medium pizza  '''  + str(aantal_Medium) + '''        ''' + str(totaalPrijs_Medium) + '''
|  Large pizza   '''    + str(aantal_Large) + '''        ''' + str(totaalPrijs_Large) + '''
---------------------------------------------------- 
|  Eindprijs = ''' + str(eindPrijs) + '''
---------------------------------------------------- ''')