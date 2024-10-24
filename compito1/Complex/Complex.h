#ifndef _COMPLEX
#define _COMPLEX
#include <iostream>

#include "TVector2.h"
#include <cmath>
#include <map>
#include <string>
#include <TGraph.h>
#include "TVector2.h"

class Complex : public TVector2
{
public:
    using TVector2 ::TVector2;
    Complex(double re, double im) : TVector2(re, im)
    {
        m_re = re;
        m_im = im;
    }

    double re() { return m_re; }
    double im() { return m_im; }

    void re(double);
    void im(double);

    double Phase();
    void SetNotation(double);
    void ChangeNotation();
    double GetNotation();
    

    Complex Coniugato();
    Complex operator*(Complex);

private:
    double m_re;
    double m_im;
    double m_n=0;
 /*   std::map<int,std::string> m_map;
    m_map[1]="esponenziale";
    m_map[0]="algebrica";
    */
}; 
std ::ostream &operator<<(std::ostream &, Complex);

#endif