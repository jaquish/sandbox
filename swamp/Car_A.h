#ifndef CAR_A_H
#define CAR_A_H

#include "ICar.h"

class Car_A : public ICar
{
    public:
    Car_A();
    Car_A(int seats);

    void printMe();
};

#endif
