#include <stdio.h>
#include "image_filter.h"

int main(void)
{
    RGBTRIPLE image[2][2] =
        {
            {{255, 0, 0},
             {0, 255, 0}},
            {{0, 0, 255},
             {255, 255, 255}}};

    printf("Before grayscale:\n");

    for (int row = 0; row < 2; row++)
    {
        for (int col = 0; col < 2; col++)
        {
            printf("Pixel [%d][%d]: R=%d G=%d B=%d\n",
                   row,
                   col,
                   image[row][col].rgbtRed,
                   image[row][col].rgbtGreen,
                   image[row][col].rgbtBlue);
        }
    }

    grayscale(2, 2, image);

    printf("\nAfter grayscale:\n");

    for (int row = 0; row < 2; row++)
    {
        for (int col = 0; col < 2; col++)
        {
            printf("Pixel [%d][%d]: R=%d G=%d B=%d\n",
                   row,
                   col,
                   image[row][col].rgbtRed,
                   image[row][col].rgbtGreen,
                   image[row][col].rgbtBlue);
        }
    }

    return 0;
}