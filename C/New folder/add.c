// #include <stdio.h>

// int main()
// {
//     int a, b;
//     printf("Enter number a:\n ");
//     scanf("%d",&a);

//     printf("Enter number b:\n");
//     scanf("%d",&b);

//     printf("The sum is %d\n", a+b);

//     return 0;
// }

#include <stdio.h>
int main()
{
    int a,b,c,d;
    a=b=c=1;
    d=++a && ++b || ++c;
    printf("\n\n\n\nA=%d\tB=%d\tC=%d\tD=%d",a,b,c,d);   

    return 0;
}
