#include <cs50.h>
#include <stdio.h>

candidate get_candidate(string prompt);

typedef struct
{
    string name;
    int votes;
}
candidate;

int main (void)
{
    candidate presedent = get_candidate("Enter candidate's name: ");

    printf("%s\n", presedent.name);
    printf("%i\n", presedent.votes);
}

candidate get_candidate(string prompt)
{
    printf("%s\n", prompt);

    candidate c;
    c.name = get_string("Enter a name: ");
    c.votes = get_int("Enter number of votes: ");

    return c;
}
