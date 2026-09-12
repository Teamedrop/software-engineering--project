#include <stdio.h>
#include "cs50.h"

typedef struct
{
    char *name;
    int number;
} data;

int main()
{
    int prompt = get_int("How many students? ");

    data student[prompt];

    for (int i = 0; i < prompt; i++)
    {
        student[i].name = get_string("Name: ");
        student[i].number = get_int("Number: ");
    }

    for (int i = 0; i < prompt; i++)
    {
        printf("%s result is %i\n ", student[i].name, student[i].number);
    }
}
