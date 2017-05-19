import time
from PIL import Image
from PIL import ImageDraw

from Adafruit_LED_Backpack import BicolorMatrix8x8


# Create display instance on default I2C address (0x70) and bus number.
display = BicolorMatrix8x8.BicolorMatrix8x8()
display.begin()

# Run through each color and pixel.
# Iterate through all colors.
#for c in [BicolorMatrix8x8.RED, BicolorMatrix8x8.GREEN, BicolorMatrix8x8.YELLOW]:
    # Iterate through all positions x and y.
#    for x in range(8):
#        for y in range(8):
            # Clear the display buffer.
#            display.clear()
            # Set pixel at position i, j to appropriate color.
#            display.set_pixel(x, y, c)
            # Write the display buffer to the hardware.  This must be called to
            # update the actual display LEDs.
#            display.write_display()
            # Delay for a quarter second.
#            time.sleep(0.25)

# Draw some colored shapes using the Python Imaging Library.

# Clear the display buffer.
display.clear()

# First create an 8x8 RGB image.
#image = Image.new('RGB', (8, 8))
image = Image.open('lokkit_icon_100')

# Then create a draw instance.
draw = ImageDraw.Draw(image)

#draw.rectangle((1, 1, 6, 6), outline=(255, 0, 0), fill=(255, 255, 0))

# Draw the image on the display buffer.
display.set_image(image)

# Draw the buffer to the display hardware.
display.write_display()

# Pause for 5 seconds
time.sleep(5)

# Clear the screen again.
display.clear()
display.set_image(display.create_blank_image())

# Make the same image scrollable
scrollable = display.horizontal_scroll(image)

# Animate the scrollable image
display.animate(scrollable)
