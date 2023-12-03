# include <stdio.h>


int main(void)
{
    // since there is no string data type in C without the cs5 library this is what it would look like 
    char *s = "HI!";
    //printf is smart enought to know the difference in what you are tring to bring by the % and s can be printed as a string or a pointer
    printf("The pointer of s is %p\n", s);
    printf("The pointer of s is %s\n", s);

    //to get the address of each character in the string, the & is to get the turn that varaibe into looking into its pointer
    printf("The pointer of s is %p\n", &s[0]);
    printf("The pointer of s is %p\n", &s[1]);
    printf("The pointer of s is %p\n", &s[2]);
    printf("The pointer of s is %p\n", &s[3]);
}