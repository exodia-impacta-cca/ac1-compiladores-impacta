import os

# abre o arquivo em modo leitura
with open ("Arthur Vinicius Santos Silva - ex03.c", "r") as file:
    alfabeto = {}

    contador_de_linhas = 0
    for linha in file:
        contador_de_linhas += 1

        for letter in linha:
            if letter in alfabeto:
                alfabeto[letter] += 1
            else:
                alfabeto[letter] = 1

tamanho_do_arquivo = str(os.stat("Arthur Vinicius Santos Silva - ex03.c").st_size)
print(f"TAMANHO DO ARQUIVO EM BYTES: {tamanho_do_arquivo}")
print("NÚMERO DE LINHAS DO ARQUIVO: " + str(contador_de_linhas))

alfabeto = dict(sorted(alfabeto.items(), key=lambda item: item[1]))

for value in alfabeto:
    print(f'{repr(value)}: {alfabeto[value]}')