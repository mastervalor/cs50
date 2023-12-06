#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Improper usage.\n");
        return 1;
    }

    //open file
    FILE *input = fopen(argv[1], "r");

    //check if file exists
    if (input == NULL)
    {
        printf("No such file found.\n");
        return 1;
    }

    typedef uint8_t BYTE;
    BYTE buffer[BLOCK_SIZE];
    size_t byteCounter;
    bool found_jpg = false;
    int count = 0;
    char filename[8];
    FILE *outfile = NULL;


    while(fread(buffer, BLOCK_SIZE, 1, input) ==1)
    {
        if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if(found_jpg)
            {
                fclose(outfile);
            }
            else
            {
                found_jpg = true;
            }
            sprintf(filename, "%03d.jpg", count);
            outfile = fopen(filename, "w");
            if (outfile == NULL)
            {
                fclose(input);
                printf("Could now create %s.\n", filename);
                return 3;
            }
            count++;
        }

        if(found_jpg)
        {
            fwrite(buffer, BLOCK_SIZE, 1, outfile);
        }
    }
    fclose(input);
    if(found_jpg)
    {
        fclose(outfile);
    }

    return 0;
}
