import os

with open ("Arthur Vinicius Santos Silva - ex03.c", "r") as file:
    numeros = []
    alfabeto = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" ,"m" ,"n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y" , "z", "1", "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0", " "]

    count = [0 for i in range(len(alfabeto))] 
    numLinhas = 0
    for linhas in file:
        numLinhas+=1
        for i in range(len(alfabeto)):
            count[i] = count[i] + linhas.count(alfabeto[i])

print("Tamanho do arquivo lido: " + str( os.stat("Arthur Vinicius Santos Silva - ex03.c").st_size) + " bytes")
print("Número de linhas do arquivo lido: " + str(numLinhas))

for i in range(len(alfabeto)):
    if(count[i]!= 0):
        print( alfabeto[i] + " : " + str(count[i]))