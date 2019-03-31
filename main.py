'''
    FILE: Main Parser
    main function
    -------------------------------------------------------------------
    Author: Carlos Antonio Mata Valdez
    Begin:28 Marzo 2019
    -------------------------------------------------------------------
'''
from Parser import Parser as Parser
from Definition import Definition as Definition

definitions = [
                Definition("negativo", "[~]"),
                Definition("coma", "[,]"),
                Definition("etiqueta", "[a-zA-Z][a-zA-Z0-9_]*"),
                Definition("llaveizq", "[{]"),
                Definition("llaveder", "[}]")]

parser = Parser(definitions)

print("**************************TEST PARSER******************************")

text = ""
while(text != "quit()"):
    print("Lista de clausulas: (Para salir tecle quit())")
    text = input()
    if text == "quit()":
        break
    else:
        clauses = parser.parse(text) #get the clauses of the text
        print(clauses)
        #print(res)
        #print("Resultado: " + res)
