from math import *
import plotly.express as px
import pandas as pd

class rocket():
    masse = 2
    runtime = 120
    tw_f = 28
    hoehe = 0
    entfernung = 0
    vh = 0
    ah = 0

    ve = 0
    ae = 0

    flugzeit = 0

class Umgebung():
    g = 9.81

u = Umgebung()
r = rocket()
T = []
H = []
E = []
VH = []
AH = []

k = 0.01 # Luftwiederstand

si = float(input("Genauigkeit (Kleiner ist genauer):  ")) #SimulationsIntervall

t = int(1000/si) # MaxSimulationsschritte

sz = 0

def TriebwerkLaufzeit(runtime,time, tw_f):
    if time >= runtime:
        return(0)
    else:
        return(tw_f)
    
def MaxHöhe(Höhe):
    maxh = 0
    for h in Höhe:
        if h > maxh:
            maxh = h
    return(maxh)

for timer in range(1,t+1):
    r.hoehe = r.hoehe+r.vh * si
    r.vh = r.vh + r.ah * si
    r.tw_f = TriebwerkLaufzeit(r.runtime, sz, r.tw_f)
    VH.append(r.vh)
    if r.ah != 0:
        r.ah = float(((r.tw_f-r.masse*u.g)/r.masse))-k*r.vh*r.vh*(r.vh/sqrt(r.vh*r.vh))
    else:
        r.ah = float(((r.tw_f-r.masse*u.g)/r.masse))
    AH.append(r.ah)
    H.append(r.hoehe)
    T.append(sz)
    
    if r.hoehe<0:
        print("Aufgekommen nach "+str(sz)+" sek Maximal Höhe: "+str(MaxHöhe(H))+" Schritte: "+str(timer))
        
        break
    sz+=si
print("Finished")

TH = pd.DataFrame({'x': T,
                   'y': H,})
TVH =pd.DataFrame({'x': T,
                   'y': VH,})
TAH =pd.DataFrame({'x': T,
                   'y': AH,})
fig1 = px.line(TH, x = 'x', y = 'y', markers = False,title = "Höhe",
              labels = {'x': 'Zeit in s', 'y':'Höhe in m'})
fig2 = px.line(TVH, x = 'x', y = 'y', markers = False,title = "Geschwindikeit",
              labels = {'x': 'Zeit in s', 'y':'Geschwindikeit in m/s'})
fig3 = px.line(TAH, x = 'x', y = 'y', markers = False,title = "Beschleunigung",
              labels = {'x': 'Zeit in s', 'y':'Beschleunigung in m/s*s'})
if input("Open Diagramm y/n -- ") == "y":
    #fig1.show()
    fig2.show()
    #fig3.show()