from math import *


# Rakete = [2,5,25] # Masse in kg, Triebwerk Laufzeeit in s, Kraft von triebwerk in n



# h = 0 #Höhe

# e = 0 #Entfernung

t = 10 # Simulationszeit

class rocket():
    masse = 2
    runtime = 5
    tw_f = 25
    hoehe = 0
    entfernung = 0


r = rocket()






Rakete = [2,5,21] # Masse in kg, Triebwerk Laufzeeit in s, Kraft von triebwerk in n

h = 0 #Höhe
H = []

e = 0 #Entfernung
E = []

t = 10 # Simulationszeit

vh = 0
ah = 0

ve = 0
ae = 0

g = 9.81

for runtime in range(0,t):
    ah = (Rakete[2]-Rakete[0]*g)/Rakete[0]
    vh = vh + ah
    h = h+vh
    H.append(h)

print(H)

    
    
