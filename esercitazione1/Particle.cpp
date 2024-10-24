#include "Particle.h"

void  Particle :: Mass(double m){ m_Mass=m; }
void Particle :: Charge(double q){ m_Charge=q;}

double Particle :: Mass(){
  return m_Mass;
}
double Particle :: Charge(){
  return m_Charge;
}
