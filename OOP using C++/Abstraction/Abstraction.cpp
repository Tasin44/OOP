#include <iostream>
#include <string>
using namespace std;

/*
 An abstract class is a class
 that cannot be instantiated (express or (to represent something on its own))
 It serves as a blueprint for other classes
 and may contain one or more pure virtual functions. (details at the end)
*/

///A class that contains at least one or more pure virtual functions is called an abstract class.

/*
A pure virtual function is declared in a base class
but does not provide an implementation.
derived classes(here Employee) must provide implementations for all
pure virtual functions to become fully functional.
*/

class AbstractEmployee {
public:
    virtual void AskForPromotion() = 0;
};

class Employee : public AbstractEmployee {//it is a derived class,who derives from AbstractEmployee
private:
    string Name;
    string Company;
    int Age;

public:
    Employee(string name, string company, int age) {
        Name = name;
        Company = company;
        Age = age;
    }

    // Override the AskForPromotion() function
    void AskForPromotion(){
        if (Age > 30)
            cout << Name << " got promoted." << endl;
        else
            cout << Name << " did not get promoted." << endl;
    }
};

int main()
{
    // Creating objects of Employee using constructor
    Employee emp1("Tasin", "Samsung", 25);
    Employee emp2("Tom", "Enosis", 45);

    emp1.AskForPromotion();//the AskForPromotion() function is called on each object
    emp2.AskForPromotion();

    /*Despite both objects using the same interface (AskForPromotion()),
    they exhibit different behaviors based on their specific implementations.
    This demonstrates polymorphic behavior, where the same interface is used to
    perform different actions depending on the actual type of the object.*/

    return 0;
}


/*

Abstraction is a fundamental concept that focuses on hiding
implementation details and exposing only essential functionalities to the user.
It allows you to create simplified models that represent complex functionalities,
making your code easier to understand, maintain, and reuse.

Core Idea:

(i) Abstraction focuses on providing a high-level view of what an object can do,
rather than how it does it.
(ii) Think of it like using a light switch. You know you can turn the light
on or off by flipping the switch,but you don't need to understand the complex electrical circuits behind it.


*/




