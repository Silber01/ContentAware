Made for LinkedIn Learning course, "Fundamentals of Dynamic Programming" by Avik Das, documentation and some code made by Das.
Course link: https://www.linkedin.com/learning/fundamentals-of-dynamic-programming/

Scales down images horizontally by using content aware resizing. Can also make the resizing process into a gif.

REQUIRED PACKAGES:
pillow (pip install pillow)
imageio (pip install imageio)

USAGE:
put input image in input folder, then in terminal run:

python3 main.py <input_name.png> <# of pixels to trim> <output_name.png>

or

python3 main.py <input_name.png> <# of pixels to trim> <output_name.png> <make_into_gif (y/n)>
If you want to choose whether to make the trimming process into a gif

Output files will be in the output folder.