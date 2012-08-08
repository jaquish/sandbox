#import <iostream>

using namespace std;

class Animal
{
public:
    void speak() { cout << "I'm a generic animal.\n";}
};

class Dog : public Animal
{
public:
    void speak() { cout << "Woof woof.\n";}
};

class Cat : public Animal
{
public:
    void speak() { cout << "Meow meow.\n";};
};

class Car
{
public:
    virtual void describe() { cout << "I'm a generic car.\n";}
};

class Chevy : public Car
{
public:
    virtual void describe() { cout << "I'm a Chevrolet.\n";}
};

class Ford : public Car
{
public:
    virtual void describe() { cout << "I'm a Ford.\n";}
};

class A
{
public:
    virtual void whoami() { cout << "class A\n"; }
};

class B : public A
{
public:
    void whoami() { cout << "class B\n"; }
};

class C : public B
{
public:
    virtual void whoami() { cout << "class C\n"; }
};

class D : public C
{
public:
    void whoami() { cout << "class D\n"; }
};

int main()
{
    Animal* a[3] = { new Animal(), new Cat(), new Dog() };

    for( int i = 0; i < 3; i ++)
    {
        a[i]->speak();
    }

    /*
        I'm a generic animal.
        I'm a generic animal.
        I'm a generic animal.
    */

    Car* c[3] = { new Car(), new Chevy(), new Ford() };

    for( int i = 0; i < 3; i++)
    {
        c[i]->describe();
    }

    /*
        I'm a generic car.
        I'm a Chevrolet.
        I'm a Ford.
    */

    c[0]->Car::describe();
    c[1]->Car::describe();
    c[2]->Car::describe();

    /*
        I'm a generic car.
        I'm a generic car.
        I'm a generic car.
    */

    A* a_a = new A();
    A* a_b = new B();
    A* a_c = new C();

    // B* b_a = new A();    // not legal
    B* b_b = new B();
    B* b_c = new C();

    // C* c_a = new A();
    // C* c_b = new B();
    C* c_c = new C();

    cout << "A* -> ....\n";
    a_a->whoami();
    a_b->whoami();
    a_c->whoami();

    cout << "B* -> ....\n";
    b_b->whoami();
    b_c->whoami();

    cout << "C* -> ....\n";
    c_c->whoami();

    cout << "A/B/C/D\n";
    A* a_d = new D();
    B* b_d = new D();
    C* c_d = new D();
    D* d_d = new D();

    a_d->whoami();
    b_d->whoami();
    c_d->whoami();
    d_d->whoami();
    
}
