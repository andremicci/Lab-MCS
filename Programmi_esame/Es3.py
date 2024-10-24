import numpy as np
import matplotlib.pyplot as plt
from ROOT import *

'''
(Esame 21/01/19) Uno spettrometro di massa misura la distanza tra il punto di ingresso degli ioni nella regione
di campo magnetico e il loro punto di rivelazione (diametro della circonferenza). Il raggio di tale circonferenza è
dato da:

dove B = 0.1 T , V = 10 3 V, q = 1.6 · 10 −19 C. Nel file Dati Spettrometro.dat sono salvati un certo numero di
valori di “diametri” corrispondenti ad un certo tempo di acquisizione di ioni.

• Si dica se la distribuzione dei dati è compatibile con l’ipotesi di singola gaussiana

• Si esegua un binned likelihood fit per determinare le due “possibili” componenti (gaussiane) e la relativa
occorrenza. Nota l’unità di massa atomica (1.66 · 10 −27 kg) si individui il numero di massa (A) degli ioni
relativi alle due componenti.
'''
       
    
    
B=0.1
v=1e03
q=1.6e-19

h=TH1D("h1","h1",40,0.555,0.59)
file= open("Dati_spettrometro.dat","r")

data=[]

for line in file:
    h.Fill(float(line))
    data.append(float(line))

f0=TF1("f0","[0]*TMath::Gaus(x,[1],[2],1)")
f0.SetParameter(0,h.GetEntries()*h.GetBinWidth(1))
f0.SetParameter(1,0.57)
f0.SetParameter(2,0.03)
h.Fit("f0","L")
p=f0.GetProb()
print("P-value=",p)
if p<0.05:
    print("Il p-value è minore di 0.05 quindi vuoldire che la probabilità di ottenere dei dati che siano meno compatibili di quelli osservati con l'ipotesi di gaussiana è minore della significanza scelta")

    

c2=TCanvas()
c2.cd()

h2=TH1D(h)
# h2.GetYaxis().SetRange(0,50)

h2.Draw()

f=TF1("f","(  TMath::Gaus(x,[0],[1],1)*(1-[4]) + TMath::Gaus(x,[2],[3],1)*[4] )*[5]")


f.SetParameter(0,0.57)
f.SetParameter(2,0.585)
f.FixParameter(5,1)
f.SetParameter(4,0.80)

f.SetParameter(3,0.03)
f.SetParameter(1,0.03)

f.SetParLimits(4,0,1)
h2.Fit(f,"0 MULTI")

mu=1.66e-27
alpha=f.GetParameter(4)*h2.GetEntries()

print("occorrenza 1",alpha)
print("occorrenza 2",h2.GetEntries()-alpha)


f.FixParameter(5,h2.GetEntries()*h2.GetBinWidth(1))
f.Draw("same")



'''
c3=TCanvas()
c3.cd()
h.Draw()
f=TF1("f","(  TMath::Gaus(x,[0],[1],1)*(1-[4]) + TMath::Gaus(x,[2],[3],1)*[4] )*[5]",0.55,0.6)


f.SetParameter(0,0.56)
f.SetParameter(2,0.585)
f.FixParameter(5,h.GetEntries()*h.GetBinWidth(1))
f.SetParameter(4,0.80)

f.SetParameter(3,0.03)
f.SetParameter(1,0.03)

f.SetParLimits(4,0,1)
h.Fit(f," L")

mu=1.66e-27
alpha=f.GetParameter(4)*h.GetEntries()

print("occorrenza 1",alpha)
print("occorrenza 2",h.GetEntries()-alpha)


'''
m1=f.GetParameter(0)**2*B**2*q/(2*v)
m2=f.GetParameter(2)**2*B**2*q/(2*v)

print("A1=",m1/mu)
print("A2=",m2/mu)
gApplication.Run(True)
