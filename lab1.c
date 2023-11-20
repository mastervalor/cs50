#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start = get_int("how many llamas are we starting with? ");
    int end;
    do
    {
        end = get_int("What is the goal number of llamas? ");
    }
    while(end < start);

    int years = 0;

    while(start < end)
    {
        start +=  start/12;
        years++;
    }

    printf("it took %i years to reach %i llamas\n", years, end);
}