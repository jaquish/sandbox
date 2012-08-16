#ifndef CAR_B_H
#define CAR_B_H

#include "ICar.h"

class Car_B : public ICar
{
    public:
    Car_B();
    Car_B(int seats);

    void printMe();
};

#endif
