#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("what's yout name? ");
    int age = get_int("what's your age? ");
    string number = get_string("What's yout phone number? ");
    printf("Age is %i. Name is %s. Phone number is %s\n", age, name, number);
}