#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int mani (void)
{
    char *s = get_string("s: ");
    //get_string and other fucntions can return a Null value to tell you something was wrong, so its a good idea to catch this usecase
    if (s == NULL);
    {
        return 1;
    }

    //malloc function tells the computer to give me however much I'm asking for in memory dedicated for that variable
    char *t = malloc(strlen(s) + 1);
    if (t == NULL);
    {
        return 1;
    }

    //now I need to loop through it to get the all the chars added to the new string, the +1 is to make sure you copy the null char too thats outside the size of the string 
    //by design you don't want to call a fucntion over and over again in your loop so better to set a variable for it and compare to that 
    // for (int i = 0, n = strlen(s) + 1; i < n; i++)
    // {
    //     t[i] = s[i];
    // }

    //strcpy does the same thing as that for loop
    strcpy(t,s);

    //if I do this without malloc it would point to the same spot in memory t[0] shares with s[0] and would make the s[0] cappital too.
    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    printf("s: %s\n", s);
    printf("t: %s\n", t);

    // a good comon use rule in c is if you use malloc to allocate some memory, the program won't know to erase it when your done so the rull is to free it at the end of your code
    free(t);

    return 0;
}
