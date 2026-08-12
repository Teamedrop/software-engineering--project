#ifndef IMAGE_FILTER_H
#define IMAGE_FILTER_H

#include <stdint.h>
#include <math.h>

typedef struct
{
    uint8_t rgbtBlue;
    uint8_t rgbtGreen;
    uint8_t rgbtRed;
} RGBTRIPLE;

void grayscale(int height, int width, RGBTRIPLE image[height][width]);

#endif