#include <cs50.h>
#include <math.h>
#include <stdio.h>

int check(long number);
string type(long num, int count);

int main(void)
{
    int count = 0;
    long card = get_long("What is your credit card number? ");
    long test = card;
    string card_type;
    while (test > 0)
    {
        test /= 10;
        count++;
    }
    if (count < 13 || count > 16)
    {
        printf("INVALID\n");
        return 0;
    }

    int valid = check(card);
    if (valid == 1)
    {
        card_type = type(card, count);
        printf("%s\n", card_type);
    }
    else
    {
        printf("INVALID\n");
    }
}

int check(long number)
{
    bool odd = false;
    int sum = 0;

    while (number > 0)
    {
        if (odd)
        {
            int digit = (number % 10) * 2;
            sum += digit / 10 + digit % 10;
            odd = false;
        }
        else
        {
            sum += number % 10;
            odd = true;
        }

        number /= 10;
    }

    return (sum % 10 == 0);
}

string type(long num, int count)
{
    if (count == 15)
    {
        int identifier = num / pow(10, 13);
        if (identifier == 34 || identifier == 37)
        {
            return "AMEX";
        }
    }
    else if (count == 16)
    {
        int identifier = num / pow(10, 14);
        if (identifier == 51 || identifier == 42 || identifier == 53 || identifier == 54 || identifier == 55)
        {
            return "MASTERCARD";
        }
    }

    if (count == 16)
    {
        int identifier = num / pow(10, 15);
        if (identifier == 4)
        {
            return "VISA";
        }
    }
    else if (count == 13)
    {
        int identifier = num / pow(10, 12);
        if (identifier == 4)
        {
            return "VISA";
        }
    }
    return "INVALID";
}
