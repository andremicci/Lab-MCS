#ifndef _ELECTRON
#define _ELECTRON
#include <iostream>
#include "Particle.h"


double const m_e=9.31e-31;
double const e=-1.602e-19;

class Electron : public Particle{
    public:
    
    Electron(): Particle(m_e,e){};

};

#endif 