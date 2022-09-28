import time

def getInput(opc: list)-> int:
    
    printOptions(opc)
    
    response = input("Escoja una opción\n")
    
    while True:
        if validation(response, len(opc)):
            return int(response)
        
        response = input("Escoja una opcion valida\n")



def printOptions(options):
    for index in range(len(options)):
        print(f'{index+1}. {options[index]}')



def validation(input, length):
    try:
        input = int(input)
        return 1 <= input <= length
    except ValueError:
        return False

def dead():
    time.sleep(2.0)
    print("Has muerto ¿Que quieres hacer?")
    gameOver = getInput(
        [
            "Volver a empezar",
            "Finalizar juego"
        ]
    )
    if gameOver == 1:
        return 
    else:
        exit()