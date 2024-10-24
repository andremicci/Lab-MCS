#include "FIFO.h"
#include <vector>

void FIFO :: push(double val){

  if((*this).size()!= m_n){
    (*this).push_back(val);}
  else{
  for(int i=0; i<m_n-1; i++) { (*this)[i]=(*this)[i+1];}
 (*this)[m_n-1]=val;}
}
 
