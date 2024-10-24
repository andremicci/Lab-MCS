#fit esponenziale binned extended scrivendo la likelihood

from   ROOT    import *
from   iminuit import Minuit
import numpy   as     np
from   math    import *

def flogl(tau,norm):
    val = 0
    for i in range(1,h.GetNbinsX()+1):
     ni=h.GetBinContent(i)
     
     #pi è l'integrale x_min^x_max
     xmin=h.GetBinLowEdge(i)
     xmax=h.GetBinLowEdge(i)+h.GetBinWidth(i)
     pi=exp(-xmin/tau)-exp(-xmax/tau)
     mui=pi*norm
     val=val -(ni*log(mui)-mui)
     
    # Definisco logl
    return val

#MAIN
h  = TH1D("h","",20,0,10)
for line in open("exp.dat"):
    h.Fill(float(line))

m = Minuit(flogl,tau=2,norm=1000)
m.errordef=0.5
m.print_level=3 #definisce il livello di informazioni printate a schermo
# Istruisco fir di logl
m.migrad()       

tau = m.values[0]
norm=m.values[1]
h.Draw()
print(tau)
# Disegno del fit
f = TF1("f","[0]*1/[1]*exp(-x/[1])",0,20)
f.SetParameter(0,norm*h.GetBinWidth(1))
f.SetParameter(1,tau)
f.Draw("SAME")

gApplication.Run(True)

#---------------------------------------------------------------------------------------------------------------------------------------------------#


















 #FIT BINNATO NON EXTENDED CON DEFINIZIONE LIKELIHOOD E CON METODI DI ROOT
def flogl(tau):
    val = 0
    for i in range(1,h.GetNbinsX()+1):

     ni=h.GetBinContent(i)
     #pi è l'integrale x_min^x_max
     xmin=h.GetBinLowEdge(i)
     xmax=h.GetBinLowEdge(i)+h.GetBinWidth(i)
     pi=exp(-xmin/tau)-exp(-xmax/tau)
     val=val-ni*np.log(pi)
            # Definisco logl
    return val

#Main
h  = TH1D("h","",20,0,10)
for line in open("exp.dat"):
    h.Fill(float(line))

m = Minuit(flogl,tau=2)
m.errordef=0.5
m.print_level=3 #definisce il livello di informazioni printate a schermo
# Istruisco fir di logl
m.migrad()       

tau = m.values[0]
h.Draw()
print(tau)
# Disegno del fit
f = TF1("f","[0]*1/[1]*exp(-x/[1])",0,20)
f.SetParameter(0,h.GetEntries()*h.GetBinWidth(1))
f.SetParameter(1,tau)
f.Draw("SAME")

f.FixParameter(0,1)
h.Fit(f,"0MULTI")
f.SetParameter(0,h.GetEntries()*h.GetBinWidth(1))
f.Draw("SAME")

gApplication.Run(True)



#---------------------------------------------------------------------------------------------------------------------------------------------------#
#FIT NON BINNATO CON TTREE
void fitexpTTree(){

  ifstream file("exp.dat");
  double x;
  TH1D *h = new TH1D("h","",40,0,10);
  while (file >> x){
    
    h->Fill(x);
  }

  TTree *t=new TTree();
  t->ReadFile("exp.dat","t/D");

  h->SetMarkerStyle(20);
  h->Draw("E");
  TF1 *fe = new TF1("fe","[0]*1/[1]*exp(-x/[1])",0,10);
  fe->SetParameter(1,2.0);
  fe->FixParameter(0,1);
   
   t->UnbinnedFit("fe","t");
   fe->SetParameter(0,h->GetEntries()*h->GetBinWidth(1));
   fe->Draw("SAME");
  
}
#---------------------------------------------------------------------------------------------------------------------------------------------------#

