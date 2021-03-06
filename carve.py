"""
The third and final step in the seam carving process: removing the lowest-energy
seam from an image. By doing so iteratively, the size of the image can be
reduced (in one dimension) by multiple pixels.

The functions you fill out in this module put together everything you've written
so far into the full seam carving algorithm. Run this module in isolation to
resize your image!

    python3 carve.py surfer.jpg 10 surfer-resized.png
"""

from energy import compute_energy
from seam_v2 import compute_vertical_seam_v2, visualize_seam_on_image
from utils import Color, read_image_into_array, write_array_into_image


def remove_seam_from_image(image, seam_xs):
    """
    Remove pixels from the given image, as indicated by each of the
    x-coordinates in the input. The x-coordinates are specified from top to
    bottom and span the entire height of the image.

    This is one of the functions you will need to implement. Expected return
    value: the 2D grid of colors. The grid will be smaller than the input by
    one element in each row, but will have the same number of rows.
    """
    i = 0
    for row in image:
        row.remove(row[seam_xs[i]])
        i += 1


def remove_n_lowest_seams_from_image(image, num_seams_to_remove, makeGif):
    """
    Iteratively:

    1. Find the lowest-energy seam in the image.
    2. Remove that seam from the image.

    Repeat this process `num_seams_to_remove` times, so that the resulting image
    has that many pixels removed in each row.

    While not necessary, you may want to save the intermediate images in the
    process, in case you want to see how the image gets progressively smaller.
    The `visualize_seam_on_image` is available if you want to visualize the
    lowest-energy seam at each step of the process.

    This is one of the functions you will need to implement. Expected return
    value: the 2D grid of colors. The grid will be smaller than the input by
    `num_seams_to_remove` elements in each row, but will have the same number of
    rows.
    """
    for i in range(num_seams_to_remove):
        energy_map = compute_energy(image)
        seam_xs, energy = compute_vertical_seam_v2(energy_map)
        remove_seam_from_image(image, seam_xs)
        print(f"{i + 1}/{num_seams_to_remove} seams removed")
        if makeGif:
            print(f'Making frame {i + 1}')
            write_array_into_image(image, "output/gifcache/" + numToBase26(i, 5) + ".jpg")
    return image


def numToBase26(num, chars):
    str = ""
    while num > 0:
        thisLetter = num % 26
        str += chr(thisLetter + 65)
        thisLetter -= thisLetter
        num = int(num / 26)
    for i in range(chars - len(str)):
        str += "A"
    return str[::-1]