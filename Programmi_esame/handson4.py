
#HANDSON4-INTERVALLI DI CONFIDENZA TEST DI IPOTESI
'''
#include <iostream>
#include <fstream>
#include <string>
#include <TApplication.h>
#include <TH1D.h>
#include <TMath.h>

using namespace std;

int main(){

  double nbkg = 44.7; 

  TApplication app("app",NULL,NULL);

  TH1D *h = new TH1D("h","",80,0,40);
  TH1D *hreg = new TH1D("hreg","",4,14,16);

  ifstream ifile("dati_highstat.dat");
  
  double mass;
  int    nobs=0;
  while (ifile >> mass){
    //calcolare nobs
    h->Fill(mass);
    if (mass>14 && mass<16){
      hreg->Fill(mass);
      nobs++;
    }
  }

  h->Draw();
  hreg->Draw("SAME");
  hreg->SetFillColor(2);

  //calcolare upper limit
int ns=0;
while(1){
      double prob=0;
      for(int i=0;i<=nobs;i++){
        prob+=TMath::PoissonI(i,nbkg+ns);

      }
      if(prob<0.05){
        cout << "Upper limit al 95% di C.L"<< ns-1 << endl;
        break;
      }
      ns++;
  }

  while(1){
      double prob=0;
      for(int i=0;i<=nobs;i++){
        prob+=TMath::PoissonI(i,nbkg+ns);

      }
      if(1-prob>0.05){
        cout << "Lower limit al 95% di C.L"<< ns-1 << endl;
        break;
      }
      ns++;
  }
  
  app.Run(true);

}
....................................................................
'''



#TEST DI IPOTESI
from   sys   import *
from   math  import *
from   ROOT  import *
import numpy as np
from   scipy import stats

file1 = open("s1.dat")
file2 = open("s2.dat")

h1 = TH1D("h1","",12,0,0.5)
h2 = TH1D("h2","",12,0,0.5)

x1 = np.array([])
for line in file1:
    val = line.split()
    x1 = np.append(x1,float(val[0]))
    h1.Fill(float(val[0]))

x2 = np.array([])
for line in file2:
    val = line.split()
    x2 = np.append(x2,float(val[0]))
    h2.Fill(float(val[0]))

h1.SetLineColor(kRed)    
h1.Draw("E")

h2.Draw("ESAME")


#scegliamo 5% come livello di significanza del test

# test del chi2
pvalue= h1.Chi2Test(h2)
print("Chi2Test:",pvalue)


# test unbinned KS 2 campioni
D,p_ks=stats.ks_2samp(x1,x2)
print(p_ks)


# test unbinned KS 1 pdf

e=stats.expon(loc=0,scale=0.1)
D1,p_ks1=stats.kstest(x1,e.cdf)
# test su esponenziale ignoto (con fit)

f = TF1("exp","[0]/[1]*exp(-x/[1])",0,0.5)

f.SetParameter(1,1) #valore settato "a caso"
h1.Fit("exp")
print("p-value Chi2()",f.GetProb())
print( "p-value Chi2()", TMath.Prob(f.GetChisquare(),h1.GetNbinsX()-1))


h1.Fit("exp","L")
print("p-value Likelihood",f.GetProb())
print( "p-value Chi2 Likelihood", TMath.Prob(f.GetChisquare(),h1.GetNbinsX()-1))

gApplication.Run(True)



