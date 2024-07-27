# cachipun.py
import sys
import random

opciones = ["piedra", "papel", "tijera"]

def jugar_cachipun(jugador):
    computador = random.choice(opciones)
    if jugador == computador:
        resultado = "Empataste!!"
    elif (jugador == "piedra" and computador == "tijera") or \
        (jugador == "papel" and computador == "piedra") or \
        (jugador == "tijera" and computador == "papel"):
        resultado = "Ganaste!!"
    else:
        resultado = "Perdiste!!"
    return computador, resultado

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Juego <piedra|papel|tijera>")
        jugador = input("Ingrese piedra, papel o tijera: ").lower()
    else:
        jugador = sys.argv[1].lower()

    if jugador not in opciones:
        print("Argumento inválido: Debe ser piedra, papel o tijera.")
    else:
        computador, resultado = jugar_cachipun(jugador)
        print(f"Tu jugaste {jugador.capitalize()}")
        print(f"Computador jugó {computador.capitalize()}")
        print(resultado)
