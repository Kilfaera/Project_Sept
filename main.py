from lib2to3.refactor import MultiprocessingUnsupported
from utils.menus import getInput
from utils.jokes import jokeSelect
import time
print("Bienvenido al juego de la vida")
response = 0
while response != 1:
    response = getInput(
        [
            "Iniciar Juego",
            "chiste sorpresa :D",
            "Salir"
        ]
    )
    if response == 1:
        print("Perfecto, vamos a iniciar")
    if response == 2:
        jokeSelect()
        time.sleep(5.0)
    elif response == 3:
        exit()

userName = input("Ingrese su nombre de usuario\n")
confirm = 2
while confirm != 1:
    print(f'¿Esta seguro de escoger {userName} como su nombre de usuario?')
    confirm = getInput([
        "Si",
        "No"
    ])
    if confirm == 2:
        userName = input("Ingrese su nombre de usuario\n")

# *******************************************************************
from utils.elections import fourthElection, startRoom, firstElection, firstElection, secondElection

nextStage = True
while nextStage:
    nextStage = firstElection(startRoom())

mind = firstElection()
print("Mente",mind)

mind += secondElection()
print("Mente",mind)
mind += fourthElection
