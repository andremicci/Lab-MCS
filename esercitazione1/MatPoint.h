#ifndef _MATPOINT
#define _MATPOINT

#include <iostream>
#include "Particle.h"
#include "Vector.h"

class MatPoint : public Particle{
  public:
  using Particle :: Particle;
  MatPoint(Particle p, Vector x, Vector v):Particle(p),m_x(x),m_v(v){}
  MatPoint(double m,double q, Vector x=Vector(), Vector v=Vector()):Particle(m,q),m_x(x),m_v(v){}
    
  

  
  void V(Vector);
  void R(Vector);

  Vector V();
  Vector R();

  Vector GravField(Vector);
 
  private:
  Vector m_x;
  Vector m_v;

  
};
#endif
