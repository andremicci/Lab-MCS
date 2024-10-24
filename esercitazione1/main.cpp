#include <iostream>
#include "Particle.h"
#include "MatPoint.h"
#include "Electron.h"
#include "Vector.h"
using namespace std;
int main(){
  Particle p1;
  p1.Mass(19);
  double m1=p1.Mass();
  cout<<m1<<endl;
  
  MatPoint M(1,0);
  
  Vector x1(1,0,0);
  M.R(x1); 
  Vector x2(1.5,0,0);
    
    Vector v=M.GravField(x2);
    cout << v.X() << endl;
  
  Electron e1;
  cout<<e1.Mass()<<endl;
  MatPoint mp(e1,x1,x2);
  cout << mp.Mass() << " "<< mp.Charge() << " "<< mp.R() <<  " "<< mp.V() << endl;
  cout << "xx"<< endl;

  Vector a(1,1,1);
  Vector b(3,2,2);
  cout << a.Cross(b) << endl;


  return 0;
}
