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

    int height = 2;
    int width = 2;
    RGBTRIPLE sepia_image[2][2] = {
        {{100, 50, 20}, {200, 150, 100}},
        {{10, 80, 160}, {255, 255, 255}}};

    printf("Before sepia:\n");

    sepia(height, width, sepia_image);
    printf("\nAfter sepia:\n");
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            printf("Pixel [%d][%d] : R=%d G=%d B=%d\n",
                   row,
                   col,
                   sepia_image[row][col].rgbtRed,
                   sepia_image[row][col].rgbtGreen,
                   sepia_image[row][col].rgbtBlue);
        }
    }
    return 0;
}
