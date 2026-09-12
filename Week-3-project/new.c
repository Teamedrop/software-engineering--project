#include <stdio.h>
#include <stddef.h>

int leng(const char *text)
{
    int length = 0;
    while (text[length] != 0)
    {
        length++;
    }
    return length;
}

char *copy(char *des, const char *src)
{
    char *new_desti = des;
    while (*src != '\0')
    {
        *des = *src;

        src++;
        des++;
    }
    *des = '\0';
    return new_desti;
}

char *join(char *des, const char *src)
{
    char *new_copy = des;
    while (*des != '\0')
    {
        *des++;
    }
    while (*src != '\0')
    {
        *des = *src;
        *des++;
        *src++;
    }
    *des = '\0';
    return new_copy;
}