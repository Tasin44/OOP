

///Polymorphism in programming is when a parent class reference is used to refer to an object of a child class
//In polymorphism,a pointer of base class will hold derived class object
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

    ///Getters to access member variables
    string getName(){
        return Name;
    }

    string getCompany(){
        return Company;
    }

    int getAge(){
        return Age;
    }
    virtual void work()
    {
        cout<<Name<<"is checking email,task backloging"<<endl;
    }
};
/*
This virtual function tell plz check if there is any implementation
of this function in any of it's derived classes,if present then execute
that function instead of base class virtual function,
if absent then base class's work() will be executed
*/

class Developer:public Employee {
public:
    string Favproglang;

    Developer(string name,string company,int age,string favproglang):Employee(name,company,age)
    {
        Favproglang=favproglang;
    }

    void work()
    {
        cout<<getName()<<" is writing: "<<Favproglang<<endl;
    }
};


class Teacher:public Employee{//by making it public,we can access Employee class form main by using.Askforpromotion

public:
///if we don't make it public,then it'll be private automatically & can't be access from main function

    string Subject;
    Teacher(string name,string company,int age,string subject):Employee(name,company,age)
    {
        Subject=subject;
    }
    void work()
    {
        cout<<getName()<<" is teaching : "<<Subject<<endl;
    }
};

int main() {
    // Creating objects of Developer using constructor
    Developer d("Tasin","BJIT", 23, "C++");

cout << "Name: " << d.getName() << " works at "<< d.getCompany()<< " is " << d.getAge() << " years & Favourite: " << d.Favproglang << endl;
//we cannot access Name,Company,Age directly here though they are protected.
//They can only access directly in that Employee class and any derived class of it


    Teacher t=Teacher("Rahim","IST",35,"Physics");

cout << "Name: " << t.getName() << " works at "<< t.getCompany()<< " is " << t.getAge() << " years & Teach students : " <<t.Subject << endl;

    Employee *e1=&d; ///Employee e1 is a base class pointer, &d is one of it's derived class object

    Employee *e2=&t;///Employee e2 is a base class pointer, &t is one of it's derived class object


    e1->work();///-> is a access modifier operator
    e2->work();


    return 0;
}



