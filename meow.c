



#include <stdio.h>
typedef struct {
    char  name[50];
    int   rollno;
    float marks;
} Student;
void displayStudent(Student s) {
    printf("Name    : %s\n",   s.name);
    printf("Roll No : %d\n",   s.rollno);
    printf("Marks   : %.2f\n", s.marks);}
int main() {
    Student s1 = {"Rahul Sharma", 101, 88.5};
    Student s2 = {"Priya Verma",  102, 92.0};
    displayStudent(s1);
    displayStudent(s2);
    return 0;
}