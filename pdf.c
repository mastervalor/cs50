#include <cs50.h>
#include <stdio.h>
#include <stdint.h>
// a program to read file signitures, which are the first bites in a file to tell us what type of file it is

int main (int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Improper usage.\n");
        return 1;
    }

    //open file
    FILE *file = fopen(argv[1], "r");

    //check if file exists
    if (file == NULL)
    {
        printf("No such file found.\n");
        return 1;
    }
    //uint8_t is a special data type. its is still an intiger
    //the u stands for unsigned, which means it will only be a positive number as a negatic(-) would mean it is signed
    //the 8 here denotes this is only 8 bits or a single byte for an integer
    //the _t just means that all of that will be its own type.
    uint8_t buffer[4];
    fread(buffer, 1, 4, file);

    for (int i = 0; 1 < 4; i++)
    {
        printf("%i", buffer[i]);
    }
}

