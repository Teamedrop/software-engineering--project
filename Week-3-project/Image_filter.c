#include "image_filter.h"

void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            int red_val = image[row][col].rgbtRed;
            int green_val = image[row][col].rgbtGreen;
            int blue_val = image[row][col].rgbtBlue;

            int average = round((red_val + green_val + blue_val) / 3.0);

            image[row][col].rgbtRed = average;
            image[row][col].rgbtGreen = average;
            image[row][col].rgbtBlue = average;
        }
    }
}