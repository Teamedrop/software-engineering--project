#include <stdio.h>
#include "cs50.h"
#include <string.h>
#include <stdlib.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int a = 10;
    int b = 20;

    swap(&a, &b);

    printf("A = %d\n ", a);
    printf("B = %d\n ", b);

    void Bubble_sort(int arr[], int size)
    {
        for (int i = 0; i < size - 1; i++)
        {
            for (int j = 0; j < size - 1 - i; j++)

                if (arr[j] > arr[j + 1])
                {
                    swap(&arr[j], &arr[j + 1]);
                }
        }
    }

    void print_array(int arra[], int sizee)
    {
        for (int i = 0; i < sizee; i++)
        {
            printf(" %d ", arra[i]);
        }
        printf("\n");
    }

    {
        int SIZES[] = {10, 5000, 20000};
        for (int i = 0; i < 3; i++)
        {
            int n = SIZES[i];
            printf("------------------------------");
            printf("Testing array of size %d\n ", n);

            int array[n];
            for (int i = 0; i < n; i++)
            {
                array[i] = rand();
            }
            if (n <= 20)
            {
                printf("Array after sorting\n");
                print_array(array, n);
            }
        }
    }
}