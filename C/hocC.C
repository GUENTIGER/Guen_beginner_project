#include<stdio.h>
#include<string.h>


struct student {
	int age;
	int grade;
	char name[40];
	
};
int main(){

	printf("hello world \n");
	/* hai bien gia tri cua struct*/
	struct student s1;
	struct student s2;
	s1.age   =18;
	s1.grade =12;
	sprintf(s1.name,"long draGON");

	s2.age   = 12;
	s2.grade = 6;
	sprintf(s2.name,"batman dc");

	printf("student: %s, %d\n",s1.name,s1.grade);
	printf("Student:%s, %d\n",s2.name,s2.grade);
	return 0;
}