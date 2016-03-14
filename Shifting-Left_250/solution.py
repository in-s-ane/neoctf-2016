from PIL import Image

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

image = Image.open("shifting_left.png").convert("RGB")
width, height = image.size
pixels = image.load()

shifted = Image.new("RGB", (width,height))
shifted_pixels = shifted.load()

for x in range(0, image.width):
    for y in range(0, image.height):
        pixel = image.getpixel((x,y))

        if pixel == RED:
            try:
                shifted.putpixel((x+9,y), RED)
            except:
                shifted.putpixel((width-1,y), RED)
        elif pixel == GREEN:
            try:
                shifted.putpixel((x+7,y), GREEN)
            except:
                shifted.putpixel((width-1,y), GREEN)
        elif pixel == BLUE:
            try:
                shifted.putpixel((x+5,y), BLUE)
            except:
                shifted.putpixel((width-1,y), BLUE)

shifted.save("shifted.png")

# flag{P1X3L_Sh1FT}
