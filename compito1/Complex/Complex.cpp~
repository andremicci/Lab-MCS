#include "Complex.h"

void Complex ::re(double re)
{
    m_re = re;
}
void Complex ::im(double im)
{
    m_im = im;
}
double Complex ::Phase()
{

    if (m_re == 0 && m_im > 0)
    {
        return M_PI / 2;
    }
    else if (m_re == 0 && m_im < 0)
    {
        return -M_PI / 2;
    }
    else if (m_re > 0)
    {
        return atan(m_im / m_re);
    }
    else if (m_re < 0 && m_im >= 0)
    {
        return atan(m_im / m_re) + M_PI;
    }
    else if (m_re < 0 && m_im <= 0)
    {
        return atan(m_im / m_re) - M_PI;
    }
    else if (m_re == 0 && m_im == 0)
    {
        return 0;
    }

   
}


void Complex ::SetNotation(double n)
{
    m_n = n;
}
double Complex ::GetNotation()
{
    return m_n;
}

Complex Complex ::Coniugato()
{
    Complex z(m_re, -m_im);
    return z;
}
Complex Complex ::operator*(Complex z)
{
    //z1=a+ib z2=c+id z1z2=(ac-bd)+i(ad+bc)
    //Complex prod(m_re*z.X()-m_im*z.Y(),m_re*z.Y()+m_im*z.X());

    Complex prod(m_re * z.m_re - m_im * z.m_im, m_re * z.m_im + m_im * z.m_re);
    return prod;
}

std ::ostream &operator<<(std::ostream &o, Complex z)
{

    if (z.GetNotation() == 0)
    {
        o << z.re() << ((z.im() > 0) ? "+i" : "-i") << fabs(z.im());
        return o;
    }
    else
    {
        //implementa
        return o;
    }
}
