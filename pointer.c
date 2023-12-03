# include <stdio.h>


int main(void)
{
    int n = 50;
    //you can call the pointer like ths
    printf("Pointer n is:  %p\n", &n);
    //or declar a variable to be a pointer
    int *p = &n;
    printf("pointer is %p\n", p);
    //to go and get the value from the pointer is poting to
    printf("pointer is %i\n", *p);
}