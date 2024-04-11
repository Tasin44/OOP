#include <iostream>
#include <string>
using namespace std;

class Employee {
private:
    string Name;
    string Company;
    int Age;

public:
    // Constructor

    Employee(string name = "", string company = "", int age = 0) : Name(name), Company(company), Age(age) {}

    // Setter functions
    void setName(string name) {
        Name = name;
    }

    void setCompany(string company) {
        Company = company;
    }

    void setAge(int age) {
        Age = age;
    }

    // Getters
    string getName(){
        return Name;
    }

    string getCompany() {
        return Company;
    }

    int getAge() {
        return Age;
    }

};

int main() {
    // Creating objects of Employee using constructor
    Employee emp1,emp2;
    emp1.setAge(39);//here we directly using setter function
    emp1.setName("Tasin");
    emp1.setCompany("YT");

    emp2.setAge(90);
    emp2.setName("Tom");
    emp2.setCompany("Enosis");

    cout << "Emp1: " << emp1.getName() << " is " << emp1.getAge() << " years old & works at: " << emp1.getCompany() << endl;
    cout << "Emp2: " << emp2.getName() << " is " << emp2.getAge() << " years old & works at: " << emp2.getCompany() << endl;

    return 0;
}

