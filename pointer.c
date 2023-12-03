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


    //you can also do pointer arithmetic, when telling it to use a pointer you can add to the memory int location to get the next part in memory
    char *s = "HI!";
    printf("The pointer of s is %c\n", *s);
    printf("The pointer of s is %c\n", *(s+1));
    printf("The pointer of s is %c\n", *(s+1));
}