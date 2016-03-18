from PIL import Image

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

image = Image.open("shifting_left.png").convert("RGB")
width, height = image.size
pixels = image.load()

shifted = Image.new("RGB", (width,height))
shifted_pixels = shifted.load()

for x in range(0, width):
    for y in range(0, height):
        pixel = image.getpixel((x,y))

        if pixel == RED:
            offset = 9
        elif pixel == GREEN:
            offset = 7
        elif pixel == BLUE:
            offset = 5
        else:
            continue

        try:
            shifted.putpixel((x+offset,y), pixel)
        except:
            # Out of bounds, so let's move it as far as we can
            shifted.putpixel((width-1,y), pixel)

shifted.save("shifted.png")

# flag{P1X3L_Sh1FT}
