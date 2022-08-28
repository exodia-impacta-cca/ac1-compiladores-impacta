import os

# abre o arquivo em modo leitura
with open ("Arthur Vinicius Santos Silva - ex03.c", "r") as file:
    numeros = []
    alfabeto = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" ,"m" ,"n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y" , "z", "1", "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0", " ", "    "]

    count = [0 for i in range(len(alfabeto))] 
    contador_de_linhas = 0
    for linhas in file:
        contador_de_linhas+=1
        for i in range(len(alfabeto)):
            count[i] = count[i] + linhas.count(alfabeto[i])

tamanho_do_arquivo = str(os.stat("Arthur Vinicius Santos Silva - ex03.c").st_size)
print(f"TAMANHO DO ARQUIVO EM BYTES: {tamanho_do_arquivo}")
print("NÚMERO DE LINHAS DO ARQUIVO: " + str(contador_de_linhas))

for i in range(len(alfabeto)):
    if(count[i]!= 0):
        print( alfabeto[i] + " : " + str(count[i]))