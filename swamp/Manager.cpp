#include "Car_A.h"
#include "Car_B.h"
#include "ICar.h"

int main()
{
    Car_A* a = new Car_A();
    Car_B* b = new Car_B();

    a->printMe();
    b->printMe();
}
