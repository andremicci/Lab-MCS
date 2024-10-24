#include <iostream>
#include <cmath>
#include <TF1.h>
#include <TApplication.h>

using namespace std;

double bisezione(TF1 f, double a, double b, double prec){
  // applica il metodo di bisezione

  double xmed;

  if (f(a)*f(b)>0){
    cout << "Attenzione funzione con stesso segno agli estremi !" << endl;
    cout << f(a) << " " << f(b) << endl; 
    exit(0);
  }

  while (fabs(b-a)>prec) {
    xmed=(a+b)/2;
    if (f(xmed)==0) {
      return xmed;
    }
    double P=f(a)*f(xmed);
    if (P<0) {
      b=xmed;
    } else {
      a=xmed;
    }
  }
  xmed = (a+b)/2;

  return xmed;

}



int main(){
  
  TApplication app("app",0L,NULL);

  TF1 f("f", "pow(x-1,3)",-3,5);
  f.Draw();
  cout << "Lo zero della Forza e' " << bisezione(f,0.1,2,1e-1) << endl;
  
  app.Run(true);

  return 0;
}
