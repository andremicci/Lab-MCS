from ROOT import *

nobs=30
n_asp=15
alpha=0.025

prob=0
for i in range(nobs):
    prob+=TMath.PoissonI(i,n_asp)

prob=1-prob
print("p-value={}".format(prob))
if prob<alpha:
    print("Ipotesi nulla rigettata")
    
n=0
while True:
    prob=0
    for i in range(nobs):
        prob+=TMath.PoissonI(i,n_asp+n)

    if prob<alpha:
        print("Upper limit al 95% di confidence level è {}".format(n-1))
        break

    n+=1

n=0
while True:
    prob=0
    for i in range(nobs):
        prob+=TMath.PoissonI(i,n_asp+n)

    if 1-prob>alpha:
        print("Lower limit al 95% di confidence level è {}".format(n-1))
        break

    n+=1

    
gApplication.Run(True)
