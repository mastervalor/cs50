#include <cs50>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int mani (void)
{
    char *s = get_string("s: ");

    //malloc function tells the computer to give me however much I'm asking for in memory dedicated for that variable
    char *t = malloc(strlen(s) + 1);

    //now I need to loop through it to get the all the chars added to the new string
    for (int i = 0; i < strlen(s) + 1; i++)
    {
        t[i] = s[i];
    }

    //if I do this without malloc it would point to the same spot in memory t[0] shares with s[0] and would make the s[0] cappital too.
    t[0] = toupper(t[0]);


    printf("s: %s\n", s);
     printf("t: %s\n", t);
}
