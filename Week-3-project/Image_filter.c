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

void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            int originalRed = image[row][col].rgbtRed;
            int originalGreen = image[row][col].rgbtGreen;
            int originalBlue = image[row][col].rgbtBlue;

            int sepiaRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            int sepiaGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            int sepiaBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);

            image[row][col].rgbtRed = (sepiaRed > 255) ? 255 : sepiaRed;
            image[row][col].rgbtGreen = (sepiaGreen > 255) ? 255 : sepiaGreen;
            image[row][col].rgbtBlue = (sepiaBlue > 255) ? 255 : sepiaBlue;
        }
    }
}