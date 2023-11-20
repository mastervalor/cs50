#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start, end;
    do
    {
        start = get_int("Start size: ");
    }
    while(start < 9);

    do
    {
        end = get_int("End size: ");
    }
    while(end < start);

    int years = 0;
    int current = start;

    while(current < end)
    {
        current += current/3 - current/4;
        years++;
    }
    
    printf("Years: %i\n", years);
    return 0;
}