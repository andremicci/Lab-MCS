import numpy as np
import random as rnd
import matplotlib.pyplot as plt
from ROOT import *
#handson 1
'''
Simulare il processo di un decadimento di una sostanza radioattiva con tempi di decadimento τ1  e τ2 la cui funzione di densità di probabilità è data da 
con τ1  = 0.1 s e τ2 = 1 s e f = 0.3 e rappresentate i tempi di decadimento in un istogramma. 
Il tempo di decadimento viene misurato con un apparato caratterizzato da un'efficienza di rivelazione (dipendente dal tempo di decadimento) data
in altri termini ogni decadimento avvenuto ad un tempo t ha una probabilità di essere misurato pari a ε (con τacc = 0.01 s) . Produrre un istogramma dei tempi 
misurati e sovrapporlo al primo.
'''
#dichiarazione generatore con TRandom3
rnd=TRandom3()
rnd.SetSeed(123344) #set sed
rnd.Rndm()          #generazione valore distribuito uniformemente tra 0 e 1

#se vuoi usare il modulo random:
#random.seed(1329)
#rdn2=random.random()   #generazione
#x=np.random.random(1000)  #creazione vettore di numeri casual di dimensione 1000


tau1=0.1
tau2=1.0
f=0.3
tauACC=0.01
sigma=0.01
ntot=10000
rnd.SetSeed(123456789)

h=TH1D("nome","titolo",100,0,5)
h1=TH1D("nome","titolo",100,0,5)
h2=TH1D("nome","titolo",100,0,5)
c1=TCanvas()

for i in range(0,ntot):
    
     if rnd.Rndm()<f:
        
        #expo con tau1 (primo tipo di esponenziale)
        t=-tau1*np.log(1-rnd.Rndm())
 
     else:
        
        #expo con tau2 (secondo tipo di esponenziale)
        t=-tau2*np.log(1-rnd.Rndm())
     
     h.Fill(t)
    
     if rnd.Rndm()<(1-np.exp(-t/tauACC)):
            treco=t+rnd.Gaus(0,sigma)
            h1.Fill(t)
            h2.Fill(treco)
     

#VOLUMI
#Calcolare il volume del solido costituito da una sfera (R=1)  con "buco" cilindro coassiale ad essa e di raggio R/2.

R=1
rc=R/2
ntot=10000
rnd2=TRandom3()
rnd2.SetSeed(13249)
Vol_sfera=(4/3)*np.pi*R**3

nacc=0

for i in range(0,ntot):
    
    x=2*R*rnd2.Rndm()-R
    y=2*R*rnd2.Rndm()-R
    z=2*R*rnd2.Rndm()-R
    
    r2=x**2+y**2+z**2
    
    rcl=x**2+y**2
    
    if r2<R**2 and rcl>rc*rc:
        
        nacc=nacc+1
        
        
p=nacc/ntot
VolMC=((2*R)**3)*p
ep=np.sqrt(p*(1-p)/ntot)
evolMC=ep*(2*R)**3


#INTEGRALI

def fun(x):
    return (np.sin(x)**3)/(1+x**2)

ntot=100000
x=np.random.rand(2,ntot)
y=fun(x[0])
acc=y[x[1]<y]
n=len(acc)
I=n/ntot


