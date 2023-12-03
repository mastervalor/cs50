# include <stdio.h>


int main(void)
{
    // since there is no string data type in C without the cs5 library this is what it would look like 
    char *s = "HI!";
    //printf is smart enought to know the difference in what you are tring to bring by the % and s can be printed as a string or a pointer
    printf("The pointer of s is %p\n", s);
    printf("The pointer of s is %s\n", s);
}