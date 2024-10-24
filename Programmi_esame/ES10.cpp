
#include "TVector2.h"
#include <iostream>
#include "TCanvas.h"
#include "TApplication.h"
#include  "TGraph.h"


using namespace std;

double const G=1;
double M;
TVector2 a(TVector2 r){
  return -G*M*(r/pow(r.Mod(),3));
}

int main(){
  TApplication *app=new TApplication("app",0,NULL);

  double x0,vy0;

  cout << "Give M,x,vy" << endl;
  cin >> M >> x0 >> vy0 ;

  TVector2 r(x0,0);
  TVector2 v(0,vy0);

  double dt=0.1;
  double tmax=300;
  double t=0;

  
  TGraph *gr=new TGraph();
  gr->SetMarkerSize(5);
  gr->SetMarkerStyle(7);
  gr->SetPoint(0,r.X(),r.Y());
  gr->Draw("AP");
  
  int ctr=1;
  while(t<tmax){

    TVector2 r_tmp;
    TVector2 v_tmp;

    r_tmp=r+v*dt;
    v_tmp=v+a(r_tmp)*dt;

    r=r_tmp;
    v=v_tmp;

    gr->SetPoint(ctr,r.X(),r.Y());
    gr->Draw("P");
    t+=dt;
    ctr++;
    
  }
  gPad->Modified();
  gPad->Update();
     

  

  app->Run(true);
  
  

}
