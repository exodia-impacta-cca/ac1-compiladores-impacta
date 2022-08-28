import os

with open ("Arthur Vinicius Santos Silva - ex03.c", "r") as file:
    alfabeto = {}

    numLinhas = 0
    for linha in file:
        numLinhas += 1

        for letter in linha:
            if letter in alfabeto:
                alfabeto[letter] += 1
            else:
                alfabeto[letter] = 0

print("Tamanho do arquivo lido: " + str( os.stat("Arthur Vinicius Santos Silva - ex03.c").st_size) + " bytes")
print("Número de linhas do arquivo lido: " + str(numLinhas))

alfabeto = dict(sorted(alfabeto.items(), key=lambda item: item[1]))
# print(alfabeto)  
for value in alfabeto:
    print(f'{value}: {alfabeto[value]}')