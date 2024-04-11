#include <iostream>
#include <string>
using namespace std;

class AbstractEmployee {
public:
    virtual void AskForPromotion() = 0;
};

class Employee :AbstractEmployee {
protected:
///Change access specifier to protected to allow access in derived classes(not the outside any of this class)
    string Name;
    string Company;
    int Age;

public:
    //Employee(string name, string company, int age) : Name(name), Company(company), Age(age) {}

    Employee(string name, string company, int age) {
        Name = name;
        Company = company;
        Age = age;
    }

    void AskForPromotion() override {
        if (Age > 30)
            cout << Name << " got promoted." << endl;
        else
            cout << Name << " did not get promoted." << endl;
    }

    // Getters to access member variables
    string getName(){
        return Name;
    }

    string getCompany(){
        return Company;
    }

    int getAge(){
        return Age;
    }
};



class Developer :public Employee {
public:
    string Favproglang;
/*
Developer class has these three properties(Name,Company,Age)
and a specific property named Favproglang ;
But these three properties(Name,Company,Age) belongs to the base(Employee)class,
Though developer class inherit from Employee class,
and this employee class has it's own constructor of (Name,Company,Age) ,
So it knows how to construct these 3 properties,
now we need to make the constructor for the specific properties of Developer class named Favproglang */

    Developer(string name,string company,int age,string favproglang):Employee(name,company,age)
    {
        Favproglang=favproglang;
    }

    void Fixbug() {// member function ,it is a method
        cout << getName() << " fixed bug using " << Favproglang << endl;
    }
};



class Teacher:public Employee{//by making it public,we can access Employee class form main by using .Askforpromotion

public://if we don't make it public,then it'll be private automatically & can't be access from main function
    string Subject;
    void preparelession()
    {
        cout<<getName()<<" is  teaching "<<Subject<<" at his class "<<endl;
    }
    Teacher(string name,string company,int age,string subject):Employee(name,company,age)
    {
        Subject=subject;
    }
};

int main() {
    // Creating objects of Developer using constructor
    Developer d("Tasin","Enosis", 23, "C++");

cout << "Name: " << d.getName() << " works at "<< d.getCompany()<< " is " << d.getAge() << " years & Favourite: " << d.Favproglang << endl;
//we cannot access Name,Company,Age directly here though they are protected.
//They can only access directly in that Employee class and any derived class of it

    d.AskForPromotion();
    d.Fixbug();

    Teacher t=Teacher("Rahim","IST",35,"Physics");

    t.preparelession();
    t.AskForPromotion();

    return 0;
}


/*
private:
When a member variable(access specifier) is declared as private within a class,
it can only be accessed by member functions of that same class.
Other classes, even those that inherit from the class(Derived class)
cannot directly access or modify the private member variables.

protected:
can access only Within the Class & any of it's Derived Classes

*/



