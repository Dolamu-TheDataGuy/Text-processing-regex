#include <stdio.h>
#include <string.h>
#include <time.h>

char *convert(char *letter)
{
    int i = 0;
    
    while (letter[i] != '\0')
    {

        if (letter[i] >= 'A' && letter[i] <= 'Z')
        {

            letter[i] += 32;
        }
        i++;
    }
    return letter;
}

int main(void)
{

    char str[200] = "";
    printf("Please enter string: ");
    scanf("%s", str);

    clock_t start, end;
    double time_taken;

    start = clock();
    convert(str);
    end = clock();
    time_taken = ((double) (end - start)) / CLOCKS_PER_SEC * 1000;
    printf("Lower case string is %s\n", str);
    printf("time taken for while loop is %f", time_taken);

    printf("\n");
    return 0;
}
