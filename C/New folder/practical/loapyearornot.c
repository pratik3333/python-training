#include <stdio.h>
int main(int argc, char const *argv[])
{
    int year;
    printf("Enter a year to check if it is leap year or not: ");
    scanf("%d",&year);
    (year%4==0 && year%100!=0)?printf("Leap year"):(year%400 == 0)?printf("Leap year"):printf("not leap year");

    return 0;
}
