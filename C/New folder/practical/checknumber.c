#include <stdio.h>
int main(int argc, char const *argv[])
{
    int no;
    printf("Enter the number you want to check it is positive or negative or equal to zero: ");
    scanf("%d",&no);

    if(no>0)
    {
        printf("Number is Positive");
        
    }
    else if(no<0)
    {
        printf("Number is Negative ");
    }
    else if (no==0)
    {
        printf("Number is Zero");
    }
    else
    {
        printf("Something went wrong");
    }
    

    return 0;
}
