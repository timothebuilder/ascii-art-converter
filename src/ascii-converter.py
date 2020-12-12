from PIL import Image, ImageDraw, ImageFont
import math

# defining the charset to be used in the ascii art
char_set = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

char_array = list(char_set)
char_length = len(char_array)
interval = char_length / 256

#! change float here to change the scale of the characters
# most times: 0.03 < scale_factor < 0.25
scale_factor = 0.09

one_char_width = 10
one_char_height = 18

def get_char(input_int):
    return char_array[math.floor(input_int * interval)]

text_file = open("Output.txt", "w")

#! change string here to change the picture to be worked on
im = Image.open("C:\\Users\\Lenovo\\Downloads\\geralt\\Netflix_Icon.jpg")
print("Image: ", im)

#! change string here to change the font to be used
font = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

# resizing the image to fit the needed scale and load the pixels to take their colors
img_width, img_height = im.size
im = im.resize((int(scale_factor * img_width),
        int(scale_factor * img_height * (one_char_width / one_char_height))),
        Image.NEAREST)
img_width, img_height = im.size
pixels = im.load()

# defining the new image for output
output_image = Image.new('RGB', (one_char_width * img_width, one_char_height * img_height),
        color = (0, 0, 0))
d = ImageDraw.Draw(output_image)
print("New image designed")

# load the pixels and add a suited character in the right color to the ouput image
# line by line starting in (0, 0)
for i in range(img_height):
    for j in range(img_width):
        if len(pixels[j, i]) == 4:
            r, g, b, a = pixels[j, i]
        else:
            r, g, b = pixels[j, i]
        h = int(r/3 + g/3 + b/3)
        pixels[j, i] = (h, h, h)
        text_file.write(get_char(h))
        d.text((j * one_char_width, i * one_char_height), get_char(h),
                font = font,
                fill = (r, g, b))
    text_file.write('\n')
    print("Got line", i, "out of", img_height - 1)

print("Outputfile written")

# saving the new image for output
output_image.save('output.png')
print("New image saved")