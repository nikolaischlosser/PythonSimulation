import plotly.express as px
import pandas as pd
import tkinter as tk
import Simulation as sim

# UI



# Erstelle eine Instanz des Hauptfensters
root = tk.Tk()

# Ändere den Titel des Hauptfensters
root.title("Raketen Simulation")
# Definiere die Eigenschaften der Rakete und ihrer Umgebung




input_Zeitschritte = tk.Entry(root, width=20, borderwidth=5, bg="#222", fg="#fff")
Label_Zeitschritte = tk.Label(root, width=20, borderwidth=5, bg="#222", fg="#fff" ,text="Zeit Schritte")

Label_Zeitschritte.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
input_Zeitschritte.grid(row=0, column=4, columnspan=2, padx=10, pady=10)

input_Zeitschritte.insert(tk.END, 1)

def Simulation():
    print(input_Zeitschritte.get())
    T,H,VH,AH,sz=sim.Simulation()
    sim.Simulation_out(T, H, VH, AH, sz)

input_Gewichtskraft = tk.Entry(root, width=20, borderwidth=5, bg="#222", fg="#fff")
Label_Gewichtskraft = tk.Label(root, width=20, borderwidth=5, bg="#222", fg="#fff" ,text="Gewichtskraft")

Label_Gewichtskraft.grid(row=0, column=8, columnspan=2, padx=10, pady=10)
input_Gewichtskraft.grid(row=0, column=16, columnspan=2, padx=10, pady=10)


input_Masse = tk.Entry(root, width=20, borderwidth=5, bg="#222", fg="#fff")
Label_Masse = tk.Label(root, width=20, borderwidth=5, bg="#222", fg="#fff" ,text="Rakete Masse")

Label_Masse.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
input_Masse.grid(row=1, column=4, columnspan=2, padx=10, pady=10)

input_Luftwiederstand = tk.Entry(root, width=20, borderwidth=5, bg="#222", fg="#fff")
Label_Luftwiederstand = tk.Label(root, width=20, borderwidth=5, bg="#222", fg="#fff" ,text="Rakete Luftwiederstand")

Label_Luftwiederstand.grid(row=1, column=8, columnspan=2, padx=10, pady=10)
input_Luftwiederstand.grid(row=1, column=16, columnspan=2, padx=10, pady=10)


input_Zeitschritte = tk.Entry(root, width=20, borderwidth=5, bg="#222", fg="#fff")
Label_Zeitschritte = tk.Label(root, width=20, borderwidth=5, bg="#222", fg="#fff" ,text="Triebwerk Kraft (N)")

Label_Zeitschritte.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
input_Zeitschritte.grid(row=2, column=4, columnspan=2, padx=10, pady=10)


input_Laufzeit = tk.Entry(root, width=20, borderwidth=5, bg="#222", fg="#fff")
Label_Laufzeit = tk.Label(root, width=20, borderwidth=5, bg="#222", fg="#fff" ,text="Triebwerk Laufzeit  (s)")

Label_Laufzeit.grid(row=2, column=8, columnspan=2, padx=10, pady=10)
input_Laufzeit.grid(row=2, column=16, columnspan=2, padx=10, pady=10)

button_simulation = tk.Button(root, text="Simulation", padx=20, pady=10 ,bg="#333", fg="#fff", command=Simulation())
button_simulation.grid(row=3, column=0)

