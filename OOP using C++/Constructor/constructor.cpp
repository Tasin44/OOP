

#include <bits/stdc++.h>
using namespace std;

class Employee{
public:
    string Name;
    string Company;
    int Age;

    void intorduce()
    {
       cout<<"Name: "<<Name<<endl;
       cout<<"company: "<<Company<<endl;
       cout<<"age :"<<Age<<endl;
    }

    //this is detailed
    Employee(string name,string company,int age)
    {
      Name=name;
      Company=company;
      Age=age;
    }

    //this is shortcut way to create constructor
    ///Employee(string name, string company, int age) : Name(name), Company(company), Age(age) {}


};

int main()
{
//constructing that object   //Invoking(calling)the constructor
   Employee emp1       =     Employee("Tasin","YT",25);
   emp1.intorduce();
   Employee emp2=Employee("Tom","Amazon",32);
   emp2.intorduce();
}

