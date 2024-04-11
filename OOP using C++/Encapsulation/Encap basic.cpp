

#include <iostream>
#include <string>
using namespace std;

class Employee {
private:
    string Name;
    string Company;
    int Age;

public:
    //this is detailed
    Employee(string name,string company,int age)
    {
      Name=name;
      Company=company;
      Age=age;
    }

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
    string getName() const {
        return Name;
    }

    string getCompany() const {
        return Company;
    }

    int getAge() const {
        return Age;
    }
};

int main() {

    // Creating objects of Employee using constructor
    Employee emp1=Employee("Tasin","YT",24);


    cout << "Emp1: " << emp1.getName() << " is " << emp1.getAge() << " years old & works at: " << emp1.getCompany() << endl;

    emp1.setAge(26);
    emp1.setName("Tasin Mahmud");
    emp1.setCompany("Samsung");
    cout << "After update: Emp1: " << emp1.getName() << " is " << emp1.getAge() << " years old & works at: " << emp1.getCompany() << endl;


    Employee emp2=Employee("Arif","BJIT",34);
    cout << "Emp2: " << emp2.getName() << " is " << emp2.getAge() << " years old & works at: " << emp2.getCompany() << endl;

    emp2.setAge(35);
    emp2.setName("Arif khan");
    emp2.setCompany("Enosis");


    cout << "After update: Emp2: " << emp2.getName() << " is " << emp2.getAge() << " years old & works at: " << emp2.getCompany() << endl;


    return 0;
}










