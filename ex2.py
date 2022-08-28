import re

with open ("Arthur Vinicius Santos Silva - ex03.c", "r") as entrada:
    alfabeto = ["main" , "auto" , "break" , "case" , "char" , "const" , "continue" , "default" , "do" , "double" , "else" , 
    "enum" ,"extern" ,"float" ,"for" ,"goto" ,"if" ,"int" ,"long" ,"register" ,"return" ,"short" ,"signed" ,"sizeof" ,"static" , "struct", "switch", "typedef" , "union" , "unsigned" , "void" , "volatile" , "while"]

    with open("ex03.out", "w+") as saida:
        for linhas in entrada:
            for reservada in alfabeto:
                linhas = re.sub(r"\b" + reservada + r"\b" , reservada.upper(), linhas)
            saida.write(linhas)
