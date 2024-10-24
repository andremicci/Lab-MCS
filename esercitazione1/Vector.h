#ifndef _VECTOR
#define _VECTOR

#include <iostream>
#include <cmath>

class Vector{
 public:
  // Vector();
  Vector(double x=0, double y=0, double z=0):m_v{x,y,z}{};
  double X();
  double Y();
  double Z();
  void X(double);
  void Y(double);
  void Z(double);

  double mod();
  Vector vers();
  
  Vector operator+(Vector);
  Vector operator-();
  Vector operator*(double);
  double operator*(Vector);
  Vector operator+=(Vector);
  Vector Cross(const Vector&) const;
  

  
 private:
  double m_v[3];
};

Vector operator*(double , Vector ); //funzione per definizione di alpha*V


std :: ostream& operator<<(std::ostream& o, Vector a);
#endif
