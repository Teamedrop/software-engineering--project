#include <stdio.h>
#include <stddef.h>

// Tell main.c about the functions in Library.c
int my_strlen(const char *str);
char *my_strcpy(char *dest, const char *src);
char *my_strcat(char *dest, const char *src);
int my_strcmp(const char *str1, const char *str2);
char *my_strchr(const char *str, char character);

int main(void)
{
    // Test my_strlen
    char text[] = "Hello";
    printf("strlen: %d\n", my_strlen(text));

    // Test my_strcpy
    char destination[50];
    my_strcpy(destination, "World");
    printf("strcpy: %s\n", destination);

    // Test my_strcat
    char first[50] = "Hello ";
    my_strcat(first, "World");
    printf("strcat: %s\n", first);

    // Test my_strcmp
    printf("strcmp: %d\n", my_strcmp("apple", "apple"));

    // Test my_strchr
    char *result = my_strchr("Hello", 'l');

    if (result != NULL)
    {
        printf("strchr: found '%c'\n", *result);
    }
    else
    {
        printf("strchr: character not found\n");
    }

    return 0;
}