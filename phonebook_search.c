#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
}
person;

int main(void)
{
    person people[2];

    people[0].name = "craid";
    people[0].number = "323";

    people[1].name = "david";
    people[1].number = "232";

    string search = get_string("Name: ");
    for(int i = 0; i < 2; i++)
    {
        if (strcmp(people[i].name, search) == 0)
        {
            printf("Found %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;
}