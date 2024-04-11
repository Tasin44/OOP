#include <bits/stdc++.h>
using namespace std;


/*
When a member variable(access specifier) is declared as private within a class,
it can only be accessed by member functions of that same class.
Other classes, even those that inherit from the class(Derived class)
cannot directly access or modify the private member variables.
*/
class Employee{
public:
    string name;
    string company;
    int Age;

    void intorduce()//member function
    {
       cout<<"Name: "<<name<<endl;
       cout<<"company: "<<company<<endl;
       cout<<"age :"<<Age<<endl;
    }

};

int main()
{

   Employee emp1;

   emp1.name="Tasin";
   emp1.company="YT";
   emp1.Age=25;

   emp1.intorduce();

   Employee emp2;

   emp2.name="Tom";
   emp2.company="YT";
   emp2.Age=34;

   emp2.intorduce();


}
