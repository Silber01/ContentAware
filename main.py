import os
import sys
import imageio.v2
from os.path import exists

from energy import compute_energy
from seam_v2 import compute_vertical_seam_v2, visualize_seam_on_image
from utils import Color, read_image_into_array, write_array_into_image
from carve import remove_n_lowest_seams_from_image


if __name__ == '__main__':
    if len(sys.argv) != 4 and len(sys.argv) != 5:
        print(f'USAGE: {__file__} <input> <num-seams-to-remove> <output> <makegif (y/n)>')
        sys.exit(1)

    makeGif = False
    if len(sys.argv) == 5:
        if (sys.argv[4] != "y" and sys.argv[4] != "n"):
            print("Put y or n for whether or not to make a gif.")
            sys.exit(1)
        else:
            makeGif = True if sys.argv[4] == 'y' else False

    input_filename = "input/" + sys.argv[1]
    num_seams_to_remove = int(sys.argv[2])
    output_filename = sys.argv[3]


    print(f'Reading {input_filename}...')
    pixels = read_image_into_array(input_filename)

    print(f'Saving {output_filename}')
    resized_pixels = remove_n_lowest_seams_from_image(pixels, num_seams_to_remove, makeGif)
    write_array_into_image(resized_pixels, "output/" + output_filename)
    if makeGif:
        gifName = "output/" + output_filename.replace(".jpg", "") + ".gif"
        images = []
        filenames = os.listdir("output/gifcache")
        filenames.sort()
        for filename in filenames:
            print(filename)
            images.append(imageio.v2.imread("output/gifcache/" + filename))

        imageio.mimsave(gifName, images)
        for filename in filenames:
            os.remove("output/gifcache/" + filename)
