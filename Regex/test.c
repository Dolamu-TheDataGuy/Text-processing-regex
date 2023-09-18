#include <stdio.h>

int main()
{
    int b = 2;

    int *ptr;

    ptr = &b;

    printf("The value of variable b is %d\n", b);
    printf("The value the ptr pointer points to is %d\n", *ptr);
    printf("The address of variable b is %p\n", &b);
    printf("The address of variable b is %p\n", ptr);
    printf("The address of pointer ptr is %p\n", &ptr);
    return 0;
}