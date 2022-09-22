from inspect import _void
import random
import string


def jokeSelect()->string:
    jokeList = ["- ¿Tienes WiFi?\n- Sí\n- ¿Y cuál es la clave?\n- Tener dinero y pagarlo.",
    "En una entrevista de trabajo:\- ¿Nivel de inglés?\n- Alto\n- Bien. Traduzca \"mirar\".\n- Look.\n- Perfecto. Úselo en una frase.\n- \"Luke\", yo soy tu padre.\n- Contratado.",
    "¿Cuál es el café más peligroso del mundo?\nEl ex-preso",
    "- Mamá, mamá, los spaghetti se están pegando.\n- Déjalos que se maten",
    "- Soy Rosa.\n- Ah, perdóname, es que soy daltónico.",
    "- Oye, ¿cuál es tu plato favorito y por qué?\n- Pues el hondo, porque cabe más comida…",
    "¿Qué pasa si tiras un pato al agua?.\nNada.",
    "- Ayer llamé a la policía porque unos ladrones robaron en mi casa y se llevaron hasta los vasos.\n- ¿Y los detuvo?\n-Sí, sí, los de tubo también.",
    "¿Cómo te llamas?\n- Lancelot.\n- Pues atrápalot…",
    "- Papá, ¿qué está más lejos, Córdoba o la Luna?.\n- Pero vamos a ver, ¿tú ves desde aquí Córdoba?"   
    ]

    print(random.choice(jokeList))