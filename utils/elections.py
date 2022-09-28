from imaplib import Int2AP
from utils.menus import getInput, dead
import time

def startRoom()->bool:
    print("Te despiertas en un cuarto deteriorado, observas por la ventana y solo ves caos en las calles, por lo que puedes notar estas en un quinto piso, Lo unico que recuerdas es que estabas escapando... No sabes de que pero sientes una gran incomodidad")
    print("¿Que vas a hacer?")
    election = 1
    gun = False
    while(election == 1 or election == 3):
        election = getInput(
            [
                "Volver a dormir",
                "Salir del cuarto",
                "Buscar en el cuarto"
            ]
        )
        if election == 1:
            print("Vuelves a dormir")
            time.sleep(2.0)
        elif election == 3:
            print("Buscas algo util en el cuarto, encuentras una pistola con ¡¡BALAS INFINITAS!!")
            time.sleep(3.0)
            gun = True
    return gun

def firstElection(gun: bool)->bool:
    print("Estas en un pasillo largo, a lo lejano observas un cadaver andante, intentas no hacer ruido pero tropiezas y te nota")
    time.sleep(2.0)
    print("El cadaver viene corriendo hacia ti, ¿que vas a hacer?")
    election = getInput(
        [
            "Atacarlo",
            "Correr",
            "Llorar como un bebe"
        ]
    )

    if election == 3:
        print("Te agachas en posicion fetal y lloras mientras el cadaver se acerca rapidamente hacia ti")
        return dead()    
    elif election == 2:
        print("Corres pero en mitad del escape de tropiezas")
        return dead()
    elif election == 1 and gun == True:
        print("Atacaste al cadaver con el arma, cayo al suelo y ¿ganaste?")
        time.sleep(2.0)
        return False
    else:
        print("Decidiste atacar a mano limpia al cadaver, era mas fuerte de lo que parecia")
        return dead()


def firstElection()->int:
    print("Descansas un momento mientras tu mente intenta procesar lo que acaba de pasar...")
    time.sleep(1.0)
    print("¿Acabas de matar a alguien?")
    time.sleep(1.0)
    print("No... Desde un principio se notaba muerto pero... y si no era asi... quien era el...")
    time.sleep(1.0)
    print("¿Que vas a hacer?")

    election = getInput(
        [
            "Observar el cadaver de cerca",
            "Ignorar el cadaver"
        ]
    )

    if election == 1:
        print("Te acercas al cadaver, por lo que puedes observar su cuerpo estaba en un estado medio de descomposición...")
        print("Tus preocupaciones disminuyen un poco... Pero no por completo... Decides intentar ver su cara, te resulta familiar")
        print("Es tu vecino, no solias hablar mucho con el debido a que unicamente salias de tu habitación para sacar la basura o ir al mercado")
        print("Pero recuerdas que era una persona alegre y que siempre intentaba ayudar a los demas...")
        print("No puedes aceptar que esto acabara asi...")
        print("Decides bajar por las escaleras")
        return 1
    elif election == 2:
        print("Decides ignorar el cadaver y solo pensar que ya no tenia salvación")
        print("Bajas las escaleras")
        return -1


def secondElection()->int:
    print("Estas en el cuarto piso")
    print("A lo lejos escuchas varios pasos bajando las escaleras, ves que es una horda de cadaveres dirigiendose hacia ti, probablemente atraidos por el ruido")
    time.sleep(3.0)
    print("¿Que vas a hacer?")
    
    election = getInput(
        [
            "Luchar contra ellos",
            "Escapar",
        ]
    )

    if election == 1:
        print("Decides dejarte llevar por la ira y luchas contra ellos")
        time.sleep(2.0)
        print("Es culpa de ellos tu situacion actual.")
        time.sleep(2.0)
        print("Es culpa de ellos el caos.")
        time.sleep(2.0)
        print("Es culpa de ellos que tu vecino...")
        time.sleep(2.0)
        print("Luchaste contra la horda entera y gracias a tu arma lograste ganar")
        time.sleep(1.0)
        print("Te sientes mas calmado")
        print("Decides bajar por las escaleras del edificio")
        return 1
    elif election == 2:
        print("Decides escapar de la horda bajando las escaleras")
        print("Corres con todas tus energias para escapar de la horda y lo logras, parece que te perdieron")
        return -1

def thirdElection()->Int2AP:
    print("Estas en el tercer piso ahora")
    print("No sabes porque la ciudad ahora es asi")
    print("Te sientes vacio")
    print("¿Que quieres hacer?")
    election = getInput(
        [
            "Orar y bajar",
            "Solo continuar bajando"
        ]
    )

    if election == 1:
        print("Te arrodillas frente a una ventana y oras a Dios")
        print("Oras por volver a tu vida normal")
        print("Oras por el bienestar de todos")
        print("Oras por tu vecino y todos los muertos")
        print("Te levantas y decides seguir bajando")
        return 1
    else:
        print("Decides solo continuar bajando")
        print("Aun te sientes nervioso por lo que puedas encontrar")
        return -1
    
def fourthElection():
    print("Estas en el segundo piso")
    print("Observas un momento atraves de una ventana, el panorama es devastador... Todo esta destruido y no ves mas que cadaveres andantes por todas las calles")
    print("¿Que vas a hacer ahora?")
    election = getInput(
        [
            "Buscar alrededor",

        ]
    )