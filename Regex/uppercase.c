#include <stdio.h>
#include <time.h>

char *convert(char *letter)
{
    int i = 0;

    for (i = 0; letter[i] != '\0'; i++)
    {

        if (letter[i] >= 'A' && letter[i] <= 'Z')
        {

            letter[i] += 32;
        }
    }
    return letter;
}

int main (void) {

    char str[200] = "";
    printf("Please enter string: ");
    scanf("%[^\n]", str);

    clock_t start, end;
    double time_taken;


    start = clock();
    convert(str);
    end = clock();
    time_taken = ((double) (end - start)) / CLOCKS_PER_SEC * 1000;
    printf("Lower case string is: %s\n", str);
    printf("the for loop took %f second to execute\n", time_taken);
    return 0;
}

