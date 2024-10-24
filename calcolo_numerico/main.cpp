#include <iostream>
#include "TApplication.h"
#include "TF1.h"
using namespace std;
int main(){

  TApplication app("app", 0,0);

  TF1 f("fun","2+x^2",0,5);
  f.Draw();
