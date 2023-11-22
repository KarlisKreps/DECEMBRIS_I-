
#Kvadrats, ko jaatrod >= 1000
minimum_square = 1000

#Mainigie
starting_number = 2
outcome = 0 
printable = 0

#Cikls while
while starting_number**2 < minimum_square:
    starting_number = starting_number+1
    print(f'Skaitlis kvadrata: {starting_number}')

#Printesana
equation = starting_number**2
print(f'Tuvakais skaitlis kvadrata lidz 1000 ir: {starting_number}, iznakums: {equation}')