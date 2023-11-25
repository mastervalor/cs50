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
    string name[] = {"craid", "david"};
    string numbers[] = {"323", "232"};

    string search = get_string("Name: ");
    for(int i = 0; i < 2; i++)
    {
        if (strcmp(name[i], search) == 0)
        {
            printf("Found %s\n", numbers[i]);
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;
}