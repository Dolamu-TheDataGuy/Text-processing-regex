#include <stdio.h>

int add_number(int *num) {
    *num += 2;
}

int main() {
    int num = 5;
    add_number(&num);
    printf("The new value of num is %d\n", num);
    return 0;
}