#include<stdio.h>
#include<conio.h>
struct student
{
char name[50];
int prn;
char branch[50];
int semester;
};
int main()
{
  printf("Enter the total number  of students:\n ");
    int n;
    scanf("%d",&n);
    struct student data[n];
    for(int i=0;i<n;i++) {
        printf("Enter  name of student(%d):\n",i+1);
        scanf("%s",data[i].name);
        printf("Enter PRN:\n ");
        scanf("%d",&data[i].prn);
        printf("Enter the branch:\n ");
        scanf("%s",data[i].branch);
        printf("Enter the semester:\n\n ");
        scanf("%d",&data[i].semester);
    }
    printf("Student Details are:\n");
    for(int i=0;i<n;i++) {
        printf("Name(%d): %s\n",i+1,data[i].name);
        printf("PRN: %d\n",data[i].prn);
        printf("Branch: %s\n",data[i].branch);
        printf("Semester of: %d\n\n",data[i].semester);
    }
    getch();
    return 0;
}