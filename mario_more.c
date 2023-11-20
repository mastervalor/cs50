#include <cs50.h>
#include <stdio.h>

void print_grid(int size);

int main(void)
{
    int height;
    do
    {
        height = get_int("how tall is the pyramid? pick between 1 and 8: ");
    }
    while (height < 1 || height > 8);

    print_grid(height);
}

void print_grid(int size)
{
    int spaces = size - 1;
    int row = 1;
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            if (spaces > j)
            {
                printf(" ");
            }

            else
            {
                printf("#");
            }
        }
        printf("  ");
        for (int j = 0; j < row; j++)
        {
            printf("#");
        }
        row++;
        spaces--;
        printf("\n");
    }
}
