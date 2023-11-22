

#Datnes nosaukums
csv_name = input("Ievadi datnes nosaukumu")

#Izveidot csv datni
with open(f'{csv_name}.csv', 'wb') as writable:
    pass

with open(f'{csv_name}.csv', 'rb') as readable:
    #Nolasa datus
    content = readable.read()
        
    #Masivs
    array = list(content)
    print(array, 'length is', len(array))

    #Piramis elements
    print(array[0])

    #Pirmie pieci elemtni
    print(array[:5])

