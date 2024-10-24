
#fit con definizione con chi2 con iminuit
from   iminuit import Minuit
import numpy as np

def f(x,a,b):
    return a*x+b
def chi2(a,b):
    val = 0
    for i in range(0,len(x)):
        val = val + ((y[i]-f(x[i],a,b))/ey[i])**2
    return val
x  = np.array([]); y  = np.array([]); ex = np.array([]); ey = np.array([])
for line in open("pendolo.dat"):
    dt  = line.split() 
    if len(dt)!=4:
        continue
    x   = np.append(x,  float(dt[0])); y   = np.append(y,  float(dt[1]))
    ex  = np.append(ex, float(dt[2])); ey  = np.append(ey, float(dt[3]))

m=Minuit(chi2,a=4,b=0)
m.migrad()
print(m.values)
print(m.errors)

###############################################################
#fit con definizione funzione e chi2 in c++ con Minuit di root
'''
using namespace std;

namespace data{
  vector<double>  x, y, ex, ey;
}

double fun(const double *x,const double *par){
  return par[0]*(*x)+par[1];
}

void fcn(int &npar, double *gin, double &f, double *par, int iflag){
  f=0.;
  for(int i=0;i<data::x.size();i++){
    f+=pow((data::y[i]-fun(&data::x[i],par))/data::ey[i],2);
  }
}

void fitlin(){
  
  ifstream file("pendolo.dat");
  double x,y,ex,ey;
  while (file >> x >> y >> ex >> ey){
    data::x.push_back(x); data::y.push_back(y); data::ex.push_back(ex); data::ey.push_back(ey);
  }

  // Define the minimization problem
  TMinuit *minuit =new TMinuit(2);
  minuit->SetFCN(fcn);

  minuit->DefineParameter(0,"a",4.0,0.01,0.,0.);
  minuit->DefineParameter(1,"b",4.0,0.01,0.,0.);

  // Minimize
   minuit->Command("MIGRAD");

  // Get result
  double a,b,ea,eb;
  minuit->GetParameter(0,a,ea);
  minuit->GetParameter(1,b,eb);
  cout << "a="<< a <<"+-"<< ea <<  endl;
  cout << "b="<< b << "+-"<< eb << endl;


}
'''
######################################################
#Se vuoi usare Minuit in python si fa cosi:
'''
from   ROOT    import *
import numpy   as np
import ctypes  as ct

def func(x,a,b):
    return a*x+b

def fcn(npar, gin, f, par,iflag):
    chi2 = 0.0
    for i in range(0,len(x)):
        chi2 += ((y[i]-func(x[i],par[0],par[1]))/ey[i])**2
    f.value = chi2

x  = np.array([]); y  = np.array([]); ex = np.array([]); ey = np.array([])

for line in open("pendolo.dat"):
    dt  = line.split()
    if len(dt)!=4:
        continue
    x   = np.append(x,  float(dt[0])); y   = np.append(y,  float(dt[1]))
    ex  = np.append(ex, float(dt[2])); ey  = np.append(ey, float(dt[3]))

minuit = TMinuit(2);
minuit.SetFCN(fcn);
minuit.DefineParameter(0,'par0',4,0.01,0.,0.)
minuit.DefineParameter(1,'par1',0,0.01,0.,0.)
minuit.Command("MIGRAD")
a  = ct.c_double(0.0); b  = ct.c_double(0.0)
ea = ct.c_double(0.0); eb = ct.c_double(0.0)
minuit.GetParameter(0,a,ea);
minuit.GetParameter(1,b,eb);

print("a = %f +- %f, b = %f +- %f"%(a.value,ea.value,b.value,eb.value))
'''



'''
FIT MULTIPLO

#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>
#include <TCanvas.h>
#include <TGraphErrors.h>
#include <TF1.h>
#include <TMinuit.h>
#include <TApplication.h>
#include <Math/Minimizer.h>
#include <Math/Functor.h>
#include <Math/Factory.h>

using namespace std;

namespace data{
  int n;
  vector<double> x1,t1,et1;
  vector<double> x2,t2,et2;
}

TF1 *f1;
TF1 *f2;

void chi2(int &npar, double *gin, double &f, double *par, int iflag){


  f=0;
  f1->SetParameters(par[0],par[1],par[2],par[3]);
  f2->SetParameters(par[0],par[1],par[4],par[5]);
  

  for(int i=0;i<data::n;i++){
    f+=pow((data::t1[i]-f1->Eval(data::x1[i]))/data::et1[i],2);
    f+=pow((data::t2[i]-f2->Eval(data::x2[i]))/data::et2[i],2);

  }
}


int main(){

  TApplication app("app",0,NULL);
  TCanvas*c=new TCanvas();
  c->cd();


  ifstream fp1("perno1.dat");
  ifstream fp2("perno2.dat");
  double tx1,tt1,tex1,tet1;
  double tx2,tt2,tex2,tet2;



  TGraphErrors gr1;
  while (fp1 >> tx1 >> tt1 >> tex1 >> tet1){
    data::x1.push_back(tx1);
    data::t1.push_back(tt1);
    data::et1.push_back(tet1);
    gr1.SetPoint(gr1.GetN(),tx1,tt1);
    gr1.SetPointError(gr1.GetN()-1,tex1,tet1);
  }

  TGraphErrors gr2;
  while (fp2 >> tx2 >> tt2 >> tex2 >> tet2){
    data::x2.push_back(tx2);
    data::t2.push_back(tt2);
    data::et2.push_back(tet2);
    gr2.SetPoint(gr2.GetN(),tx2,tt2);
    gr2.SetPointError(gr2.GetN()-1,tex2,tet2);
  }
  data::n=data::x1.size();

  f1 = new TF1("f1","[2]*(x-[0])^2+[3]*(x-[0])+[1]",data::x1[0],data::x1[data::n-1]);
  f2 = new TF1("f2","[2]*(x-[0])^2+[3]*(x-[0])+[1]",data::x1[0],data::x1[data::n-1]);

  gr1.Fit("f1");
  gr2.Fit("f2");
  gr1.Draw("AP");
  gr2.Draw("P");
 // app.Run(true);

  // Minuit
  TMinuit minuit(6);
  minuit.SetFCN(chi2);
  minuit.DefineParameter(0,"x0",36,0.01,0,0);
  minuit.DefineParameter(1,"T0",4,0.01,0,0);
  minuit.DefineParameter(2,"a1",f1->GetParameter(2),0.01,0,0);
  minuit.DefineParameter(3,"b1",f1->GetParameter(3),0.01,0,0);
  minuit.DefineParameter(4,"a2",f2->GetParameter(2),0.01,0,0);
  minuit.DefineParameter(5,"b2",f2->GetParameter(3),0.01,0,0);
  minuit.Command("MIGRAD");

  f1->SetLineColor(kBlue);
  f1->Draw("SAME");
  c->Modified();
  c->Update();


  app.Run(true);

  return 0;

}
'''
