'''
    FILE: Main Parser
    main function
    -------------------------------------------------------------------
    Author: Carlos Antonio Mata Valdez
    Begin:28 Marzo 2019
    -------------------------------------------------------------------
'''
from Parser import Parser as Parser

print("**************************TEST PARSER******************************")

parser = Parser()
text = ""
while(text != "quit()"):
    print("Lista de clausulas: (Para salir tecle quit())")
    text = ""  #input()
    if text == "quit()":
        break
    else:
        clauses = parser.parse(text) #get the clauses of the text
        print(clauses)
