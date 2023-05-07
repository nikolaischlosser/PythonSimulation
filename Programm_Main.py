import Simulation as Sim 

T , H, VH, AH, Simulstions_Zeit = Sim.Simulation(float(input("Genauigkeit (Kleiner ist genauer):  ")))
Sim.Simulation_out(T, H, VH, AH, Simulstions_Zeit)
Sim.open_diagramm(T , H, VH, AH)