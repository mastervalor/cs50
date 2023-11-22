// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

string replace(string word);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Missing command line argument");
        return 1;
    }
    else
    {
        printf("%s\n", replace(argv[1]));
    }
}

string replace(string word)
{
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        if(word[i] == 'a' || word[i] == 'A')
        {
            word[i] = '6';
        }
        else if(word[i] == 'e' || word[i] == 'E')
        {
            word[i] = '3';
        }
        else if(word[i] == 'i' || word[i] == 'I')
        {
            word[i] = '1';
        }
        else if(word[i] == 'o' || word[i] == 'O')
        {
            word[i] = '0';
        }
    }
    return word;
}
