
#include <iostream>
#include "MatPoint.h"
#include "Vector.h"
#include <cmath>


/*MatPoint :: MatPoint(Particle p, Vector x, Vector v){
  m_mass=p.Mass();
  m_charge=p.Charge();
  m_x=x;
  m_v=v;
}*/

void MatPoint :: V(Vector v){ m_v=v;}
void MatPoint :: R(Vector x){m_x=x;}



Vector MatPoint :: V(){
  return m_v;}

Vector MatPoint :: R(){
  return m_x;}

Vector MatPoint :: GravField(Vector r){
  
  Vector r_primo=m_x;
  Vector r_corsivo=r+(-r_primo);
  double mod_rcorsivo= r_corsivo.mod();
  double M=(*this).Mass();
  double const G=6.7e-11;
  return -r_corsivo*(M*pow(1/mod_rcorsivo,3));
  }
  
  
