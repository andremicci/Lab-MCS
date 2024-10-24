from ROOT import *
import math
import numpy as np


g=TGraph()
c1 = TCanvas( 'c1', 'A Simple Graph Example', 200, 10, 700, 500 )
c1.DrawFrame(0,-2,100,2)

c1.SetFillColor( 42 )
c1.SetGrid()
t=0
dt=1
for i in range(0,100):
    g.SetPoint(i,t,np.sin(t))
    t=t+dt
    g.Draw("Pl")
    c1.Modified()
    c1.Update()
    
gApplication.Run()