#Instituto Superior Universitario "ITECSUR"

#Carrera: Desarrollo de Software  "Tercer Semestre"

# Edison Cabezas 

import tkinter as tk   #Empezamos importando las librerias Tkinter para poder representa de forma grafica
import random          #La libreria Random, nos sirve para que la computadora elija al azar, la opcion

class PiedraPapelTijeraApp:   # Creamos la clase PiedraPapelTijera
    def __init__(self, root):  #Definimos init, para que que se inicialicen los componentes de la interfaz
        self.root = root
        self.root.title("Piedra, Papel o Tijera") 
        self.root.geometry("400x450")  #  Aqui definimos las dimensiones de la ventana
        self.root.configure(bg="#008000")  # Escogemos el color del fondo de nuestra aplicacion 

        
        self.jugador_puntuacion = 0  # Aqui definimos las variables de puntuacion para el jugador 
        self.computadora_puntuacion = 0   # Aqui definimos las variables de puntuacion para la computadora

        # Definimos el titulo de nuestro juego
        tk.Label(root, text="Piedra, Papel o Tijera", font=("Castellar", 18), bg="#f0f8ff", fg="#333333").pack(pady=10)

        # Aqui empiezan las opciones del jugador 
        self.botones_frame = tk.Frame(root, bg="#008000")
        self.botones_frame.pack(pady=20)

        tk.Button(self.botones_frame, text="Piedra", command=lambda: self.jugar("Piedra"), width=10, bg="#add8e6", fg="#000000").grid(row=0, column=0, padx=10)
        tk.Button(self.botones_frame, text="Papel", command=lambda: self.jugar("Papel"), width=10, bg="#add8e6", fg="#000000").grid(row=0, column=1, padx=10)
        tk.Button(self.botones_frame, text="Tijera", command=lambda: self.jugar("Tijera"), width=10, bg="#add8e6", fg="#000000").grid(row=0, column=2, padx=10)

        # En este apartado mostramos los resultados 
        self.resultado_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff", fg="#333333")
        self.resultado_label.pack(pady=10)

        # En  esta parte la computadora escoje la opcion, para seguir jugando.
        self.seleccion_computadora_label = tk.Label(root, text="La computadora eligió: ", font=("Arial", 12), bg="#f0f8ff", fg="#333333")
        self.seleccion_computadora_label.pack(pady=10)

        # Mostramos la puntuacion del juego 
        self.puntuacion_label = tk.Label(root, text="Jugador: 0 | Computadora: 0", font=("Arial", 12), bg="#f0f8ff", fg="#333333")
        self.puntuacion_label.pack(pady=10)

    def jugar(self, eleccion_jugador):
        
        opciones = ["Piedra", "Papel", "Tijera"]
        eleccion_computadora = random.choice(opciones)

        # Aqui se siguen actualizando las opciones de la computadora 
        self.seleccion_computadora_label.config(text=f"La computadora eligió: {eleccion_computadora}")

        # En este apartado determinamos el resultado, del juego 
        if eleccion_jugador == eleccion_computadora:
            resultado = "Empate"
        elif (
            (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijera") or
            (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra") or
            (eleccion_jugador == "Tijera" and eleccion_computadora == "Papel")
        ):
            resultado = "Ganaste"
            self.jugador_puntuacion += 1
        else:
            resultado = "Perdiste"
            self.computadora_puntuacion += 1

        # Actualizar el resultado y las puntuaciones
        self.resultado_label.config(text=f"Resultado: {resultado}")
        self.puntuacion_label.config(text=f"Jugador: {self.jugador_puntuacion} | Computadora: {self.computadora_puntuacion}")

# Crear la ventana principal
root = tk.Tk()
app = PiedraPapelTijeraApp(root)
root.mainloop()

