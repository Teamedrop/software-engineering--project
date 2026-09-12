#include <stdio.h>
#include <stddef.h>

int leng(const char *text);
char *copy(char *des, const char *src);
char *join(char *des, const char *src);

int main()
{
    // for length
    char input[] = "Hello";
    int result = leng(input);
    printf("Length: %d\n", result);

    // for copying
    char destination[] = "Surname";
    char source[] = "Names";

    copy(destination, source);
    printf("Copied: %s\n ", destination);

    // Test my_strcat
    char first[50] = "Hello ";
    join(first, "World");
    printf("strcat: %s\n", first);
}