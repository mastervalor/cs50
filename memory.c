#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i\n", x, y);
    //you have to give it & to give it the address
    swap(&x, &y);
    printf("x is %i, y is %i\n", x, y);
}


//without the making a and b a pointer they will create thier own slot in memory, swap to them selfs and leave x and y as is
//so you need to make them pointers so that they swap values on x and y instead of in their own memory.
void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}