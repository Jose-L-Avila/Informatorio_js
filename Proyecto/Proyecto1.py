
# El juego debe tener una lista de palabras predefinidas de las cuales se
# elige una palabra aleatoriamente para que el jugador adivine.
from random import randint
from GraficoAhorcado import imprimirAhorcado

palabras = ["messi", "casa", "auto", "maradona", "river", "bicicleta"]
indice_palabras_max = len(palabras) - 1
indice_aleatorio = randint(0, indice_palabras_max)

palabra_aleatoria = palabras[indice_aleatorio] # palabra aleatoria

# El jugador tiene un número limitado de intentos para adivinar la palabra
# (por ejemplo, 6 intentos).
intentos = 6
# Debe mostrar las letras adivinadas y las letras incorrectas.
correctas = []
incorrectas = []
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
palabra_secreta = ['?'] * len(palabra_aleatoria)
print(palabra_secreta)
print(palabra_aleatoria)
print(f"{imprimirAhorcado(intentos)}")
# El juego debe verificar si la letra ingresada por el jugador está en la
# palabra secreta y actualizar el estado del juego en consecuencia.

while intentos > 0:
    letra_ingresada =input("\nPor favor ingrese una letra: ")
    letra_ingresada= letra_ingresada.lower()
    if letra_ingresada in letras:
        ind = 0
        existe_letra = False
        for letra in palabra_aleatoria: # messi
            if letra == letra_ingresada:
                existe_letra = True
                palabra_secreta[ind] = letra_ingresada
                print(f"La letra pertenece a la palabra secreta y se ubica en la posicion {ind+1}.") 
                correctas.append(letra_ingresada)               
            ind += 1

        if existe_letra:
            letras.remove(letra_ingresada)
            print(f"{imprimirAhorcado(intentos)}")
            print(palabra_secreta)  
            
        else:
            incorrectas.append(letra_ingresada)
            intentos -= 1
            print(f"La letra ingresada no pertenece a la palabra secreta, aun tienes {intentos} intentos.")
            print(f"Letras incorrectas ingresadas: {incorrectas}")
            print(f"{imprimirAhorcado(intentos)}")
            print(palabra_secreta)

    if(len(correctas) == len(palabra_aleatoria)):
        print(f"¡Felicitaciones completaste la palabra secreta! ({palabra_aleatoria})")
        print(f"{imprimirAhorcado(7)}")
        break

if intentos == 0:
    print("Te quedaste sin intentos, te deseo mas suerte en tu proximo juego por el bien del muñeco.")
    print(f"{imprimirAhorcado(0)}")


   
# El juego debe terminar cuando el jugador adivine la palabra o se quede
# sin intentos.
# Debe mostrar un mensaje de victoria o derrota al final del juego.
# Opcional: debe mostrar una representación gráfica del estado actual del
# ahorcado. Puedes usar arte ASCII para esto.