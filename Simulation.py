from math import *


# Rakete = [2,5,25] # Masse in kg, Triebwerk Laufzeeit in s, Kraft von triebwerk in n



# h = 0 #Höhe

# e = 0 #Entfernung

t = 10 # Simulationszeit

class rocket():
    masse = 2
    runtime = 20
    tw_f = 34
    hoehe = 0
    entfernung = 0
    vh = 0
    ah = 0

    ve = 0
    ae = 0

class Umgebung():
    g = 9.81
u = Umgebung()
r = rocket()

H = []
E = []

t = 1000 # Simulationszeit

def TriebwerkLaufzeit(runtime,time, tw_f):
    if time >= runtime:
        return(0)
    else:
        return(tw_f)

for timer in range(1,t+1):
    r.ah = (r.tw_f-r.masse*u.g)/r.masse
    r.vh = r.vh + r.ah
    r.hoehe = r.hoehe+r.vh
    H.append(r.hoehe)
    r.tw_f = TriebwerkLaufzeit(r.runtime, timer, r.tw_f)
    if r.hoehe<=0:
        print(H)
        print("Aufgekommen nach "+str(timer)+" sek")
        break
        


    
    
