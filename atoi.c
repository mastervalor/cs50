#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    // TODO
    int length = strlen(input) - 1;
    int number = input[length] - '0';
    int answer = 0;

    if (length == 0)
    {
        return number;
    }

    input[length] = '\0';

    answer = convert(input);
    answer = answer * 10 + number;

    return answer;
}
