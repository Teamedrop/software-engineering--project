#include <stdio.h>
#include <stddef.h>

// String length
int my_strlen(const char *str)
{
    int length = 0;

    while (str[length] != '\0')
    {
        length++;
    }
    return length;
}

// String copy
char *my_strcpy(char *dest, const char *src)
{
    char *original_dest = dest;

    while (*src != '\0')
    {
        *dest = *src;

        dest++;
        src++;
    }

    *dest = '\0';
    return original_dest;
}

// String joining
char *my_strcat(char *dest, const char *src)
{
    char *original_destination = dest;

    while (*dest != '\0')
    {
        dest++;
    }

    while (*src != '\0')
    {
        *dest = *src;

        dest++;
        src++;
    }

    dest = '\0';
    return original_destination;
}

// String compare
int my_strcmp(const char *str1, const char *str2)
{
    while (*str1 != '\0' && *str2 != '\0' && *str1 == *str2)
    {
        str1++;
        str2++;
    }

    if (*str1 != *str2)
    {
        return (unsigned char)*str1 - (unsigned char)*str2;
    }
    return 0;
}

// Find string
char *my_strchr(const char *str, const char character)
{
    while (*str != '\0')
    {
        if (*str == character)
        {
            return (char *)str;
        }
        str++;
    }

    if (character == '\0')
    {
        return (char *)str;
    }
    return NULL;
}