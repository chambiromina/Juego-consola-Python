
import random
from clases.enemigo import Enemigo
from clases.jugador import Jugador


def main():
    nombre_jugador = input("¡Bienvenido a la aventura en el Espacio! Por favor, ingresa tu nombre: ")
    
    jugador = Jugador(nombre_jugador)
    
    Enemigos = [Enemigo("alien", 50, 10),
                Enemigo("Robot", 30, 5),
                Enemigo("Monstruo", 70, 15)
    ]
    print("¡Comienza la Avetura!")

    while True:
        Enemigo_actual = random.choice(Enemigos)
        print(f"Te encuentras con un {Enemigo_actual.nombre} en tu camino")

        while Enemigo_actual.salud > 0:
            accion = input("Que deseas hacer? (ataca/huir): ").lower()

            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(f"Has atacado al {Enemigo_actual.nombre} y le has causado {dano_jugador} de daño")
                Enemigo_actual.recibir_dano(dano_jugador)

                if Enemigo_actual.salud > 0:
                    dano_enemigo = Enemigo_actual.atacar()
                    print(f"El {Enemigo_actual.nombre} te ataco y te causo {dano_enemigo} de daño")
                    jugador.recibir_dano(dano_enemigo)

            elif accion == "huir":
                    print("¡Has decidido huir del combate!")
                    break
            
        if jugador.salud <= 0:
                print("¡Has perdido la partida!")
                break

        jugador.ganar_experiencia(20)

        continuar =input("¿Quieres seguir explorando (s/n): ").lower()

        if continuar != "s":
            print("¡gracias por haber jugado estas batallas")
            break

if __name__ == "__main__":
    main()