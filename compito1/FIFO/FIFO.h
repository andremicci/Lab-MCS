#ifndef _FIFO
#define _FIFO


#include <vector>
#include <iostream>
#include "TVector2.h"
#include <cmath>
#include <TGraph.h>


class FIFO : public std::vector<double>{
  public:
  using vector :: vector;
  FIFO(int n): vector<double>(){
    m_n=n;
  }

  void push(double);
        
   private:
        int m_n;
       
};

#endif
