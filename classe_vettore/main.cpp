#include "Vector.h"
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>

using namespace std;

bool fun(Vector a, Vector b){
  return a.mod()<b.mod();}

int main(){
  

  string filename;
  cout << "Inserire nome file:" << endl;
  cin >> filename;

  ifstream file(filename);
  double x,y,z;

  vector <Vector> v;

  while(file >> x >> y >> z){
    Vector s(x,y,z);
    v.push_back(s);
  }

  sort(v.begin(),v.end(), fun);
  for( auto x: v) cout << x <<" " << x.mod() << endl;

  Vector sum;
  for(auto x: v) sum+=x;
  cout << "il vettore somma è:"<< sum << endl;
  
  
    
    
  return 0;
  
}
