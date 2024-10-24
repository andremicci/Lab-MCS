#include <iostream>
#include "TF1.h"
using namespace std;

double Estremo(TF1 f,double a,double b,double c,double prec){


  if(f(b)<f(a) && f(b)<f(c) && a<b<c ==0){
    cout << "Condizioni di partenza non soddisfatte" << endl;
    exit(0);
}

    double x=0;
    
    while(1){

      double Ir=fabs(c-b);
      double Il=fabs(b-a);

      if(Ir>Il) x=(c+b)/2.0;
      else x=(a+b)/2.0;

      cout << x << endl;
      
      if(f(x)>f(b)){
	c=x;
      }
      else{
	a=b;
	b=x;}

      if(fabs(a-c)<prec) break;
      
       
    }
    return b;
}

int main(){


  TF1 f("f","pow(x-3,2)",0,10);
  cout << Estremo(f,2,5,7,0.01) << endl;
  
}
