from math import *
import plotly.express as px
import pandas as pd
import tkinter as tk


# Definiere die Eigenschaften der Rakete und ihrer Umgebung
class Rakete():
    masse = 2
    runtime = 60
    tw_f = 40
    hoehe = 0
    entfernung = 0
    vh = 0
    ah = 0
    Luftwiderstand = 0.01

    flugzeit = 0

class Umgebung():
    g = 9.81

u = Umgebung()
r = Rakete()

# Funktion zum Überprüfen der Laufzeit des Triebwerks
def TriebwerkLaufzeit(runtime, time, tw_f):
    if time >= runtime:
        return(0)
    else:
        return(tw_f)

# Funktion zum Finden der maximalen Höhe
def MaxHöhe(Höhe):
    maxh = 0
    for h in Höhe:
        if h > maxh:
            maxh = h
    return(maxh)

# Schleife für die Simulation
def Simulation(si):
        # Speichere die Daten der Simulation
    T = []
    H = []
    VH = []
    AH = []

    # Berechne die Anzahl der Simulationsschritte
    t = int(1000/si)
    k = r.Luftwiderstand
    # Initialisiere den Zeitschritt
    sz = 0
    for timer in range(1,t+1):
        # Berechne die Höhe und Geschwindigkeit der Rakete
        r.hoehe = r.hoehe+r.vh * si
        r.vh = r.vh + r.ah * si

        # Überprüfe, wie lange das Triebwerk laufen soll
        r.tw_f = TriebwerkLaufzeit(r.runtime, sz, r.tw_f)

        # Berechne die Beschleunigung der Rakete
        VH.append(r.vh)
        if r.ah != 0:
            r.ah = float(((r.tw_f-r.masse*u.g)/r.masse))-k*r.vh*r.vh*(r.vh/sqrt(r.vh*r.vh))
        else:
            r.ah = float(((r.tw_f-r.masse*u.g)/r.masse))
        AH.append(r.ah)
        H.append(r.hoehe)
        T.append(timer)

        # Überprüfe, ob die Rakete auf dem Boden angekommen ist
        if r.hoehe<0:
            break
        sz+=si

    return T,H,VH,AH,sz

# Ausgabe der Simulation
def Simulation_out(T,H,VH,AH,sz):
    print("Simulation completed")
    print("Maximum height: "+str(MaxHöhe(H))+" meters")
    print("Maximum velocity: "+str(max(VH))+" meters/second")
    print("Maximum acceleration: "+str(max(AH))+" meters/second^2")
    print("Total flight time: "+str(sz)+" seconds")
def open_diagramm(T , H, VH, AH):
    # Erstelle Datenrahmen und Diagramme mit Plotly
    TH = pd.DataFrame({'x': T, 'y': H})
    TVH =pd.DataFrame({'x': T, 'y': VH})
    TAH =pd.DataFrame({'x': T, 'y': AH})
    fig1 = px.line(TH, x = 'x', y = 'y', markers = False,title = "Höhe",
                labels = {'x': 'Zeit in s', 'y':'Höhe in m'})
    fig2 = px.line(TVH, x = 'x', y = 'y', markers = False,title = "Geschwindikeit",
                labels = {'x': 'Zeit in s', 'y':'Geschwindikeit in m/s'})
    fig3 = px.line(TAH, x = 'x', y = 'y', markers = False,title = "Beschleunigung",
                labels = {'x': 'Zeit in s', 'y':'Beschleunigung in m/s*s'})
    if input("Open Diagramm y/n -- ") == "y":
        fig1.show()
        fig2.show()
        fig3.show()