#include <stdio.h>
#include "cs50.h"

void sort_array(int array[], int size);

int main()
{
    int size = get_int("How many values:");

    int numbers[size];

    for (int i = 0; i < size; i++)
    {
        numbers[i] = get_int("Your number: ");
    }

    printf("Before sorting\n");
    for (int i = 0; i < size; i++)
    {
        printf("%i ", numbers[i]);
        printf("\n");
    }

    sort_array(numbers, size);

    printf("After sorting\n");
    for (int i = 0; i < size; i++)
    {
        printf("%i", numbers[i]);
    }
}

// Bubble sort function
void sort_array(int array[], int size)
{
    int outter_index, inner_index, temp;
    for (outter_index = 0; outter_index < size - 1; outter_index++)
    {
        for (inner_index = 0; inner_index < size - outter_index - 1; inner_index++)
        {
            if (array[inner_index] > array[inner_index + 1])
            {
                temp = array[inner_index];
                array[inner_index] = array[inner_index + 1];
                array[inner_index + 1] = temp;
            }
        }
    }
}
