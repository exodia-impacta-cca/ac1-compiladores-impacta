# - ler o arquivo em C
# - Iterar sobre o arquivo e encontrar as palavras reservadas
# - Colocar as palavras reservadas em MAIÚSCULO 
# - Salvar no arquivo

import re

with open ("Arthur Vinicius Santos Silva - ex03.c", "r") as file, open("ex03.out", "w+") as writefile:
    alfabeto = ["main" , "auto" , "break" , "case" , "char" , "const" , "continue" , "default" , "do" , "double" , "else" , 
    "enum" ,"extern" ,"float" ,"for" ,"goto" ,"if" ,"int" ,"long" ,"register" ,"return" ,"short" ,"signed" ,"sizeof" ,"static" , "struct", "switch", "typedef" , "union" , "unsigned" , "void" , "volatile" , "while"]
    
    # for linhas in file:
    #     for i in range(len(alfabeto)):
    #         linhas = linhas.replace(alfabeto[i], alfabeto[i].upper())
    #     writefile.write(linhas)

    for linhas in file:
        for i in range(len(alfabeto)):
            regex = r"\b" + alfabeto[i] + r"\b"  
            linhas = re.sub(regex, alfabeto[i].upper(), linhas)
        writefile.write(linhas)
