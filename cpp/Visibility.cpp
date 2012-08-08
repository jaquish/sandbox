#include <iostream>

using namespace std;

class A
{
private:
int _a;

public:
A(int a) { _a = a;}; 
void printA(A* instance) { cout << instance->_a; }

};

int main()
{
	A* a1 = new A(5);
	A* a2 = new A(10);
	a1->printA(a2);
}
