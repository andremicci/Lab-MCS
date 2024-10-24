#ifndef _PARTICLE
#define _PARTICLE
#include <iostream>

class Particle{

public:

  Particle( double Mass=0,double Charge=0){
    m_Mass=Mass;
    m_Charge=Charge;} 
  double Mass();
  double Charge();
  void Mass(double);
  void Charge(double);

protected:
  double m_Mass;
  double m_Charge;
};

#endif
