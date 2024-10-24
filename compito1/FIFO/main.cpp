#include "FIFO.h"
#include <iostream>
#include <vector>

using namespace std;

//Programma di test

int main()
{
    FIFO a(5);
    FIFO b(3);

    for (double i = 0; i < 10; i++)
    {
        b.push(i);
    }

    a.push(5);
    a.push(6);

    for (int i = 0; i < 3; i++)
    {
        cout << b[i] << endl;
    }

    return 0;
}
