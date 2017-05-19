# -*- coding: utf-8 -*-

"""Console script for ledmatrix."""

import click

import time
from PIL import Image
from PIL import ImageDraw
from random import randint

from Adafruit_LED_Backpack import BicolorMatrix8x8

# Create display instance on default I2C address (0x70) and bus number.
display = BicolorMatrix8x8.BicolorMatrix8x8()
# Initialize the display. Must be called once before using the display.
display.begin()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('num', type=int)
def boot(num):
    """ Show boot sequence on screen """
    _boot(num)

def _boot(num):
    _roll_the_number(100)
    for x in xrange(4):
        _number(num)
        time.sleep(0.4)
        _inverse_number(num)
        time.sleep(0.4)
    _number(num)

@cli.command()
@click.argument('number', type=int)
def dice(number):
    _dice(number)

def _dice(number):
    display_image(Image.open('ledmatrix/dice_{}.png'.format(number)).rotate(90))

@cli.command()
@click.argument('number', type=int)
def inverse_dice(number):
    _inverse_dice(number)

def _inverse_dice(number):
    display_image(Image.open('ledmatrix/dice_inverse_{}.png'.format(number)).rotate(90))

@cli.command()
@click.argument('iterations', type=int)
def roll_the_dice(iterations):
    _roll_the_dice(iterations)

def _roll_the_dice(iterations):
    lastint = 0
    for x in xrange(iterations):
        rnd = randint(1, 6)
        while rnd == lastint:
            rnd = randint(1, 6)
        lastint = rnd
        display_image(Image.open('ledmatrix/dice_{}.png'.format(rnd)).rotate(90))
        time.sleep(0.1)
    display.clear()
    display.write_display()

@cli.command()
@click.argument('iterations', type=int)
def roll_the_number(iterations):
    _roll_the_number(iterations)

def _roll_the_number(iterations):
    lastint = 0
    for x in xrange(iterations):
        rnd = randint(1, 6)
        while rnd == lastint:
            rnd = randint(1, 6)
        lastint = rnd
        display_image(Image.open('ledmatrix/number_{}.png'.format(rnd)).rotate(90))
        time.sleep(0.1)
    #display.clear()
    #display.write_display()

@cli.command()
@click.argument('x', type=int)
def number(x):
    _number(x)

def _number(x):
    """Display number x on screen."""
    display_image(Image.open('ledmatrix/number_{}.png'.format(x)).rotate(90))

@cli.command()
@click.argument('x', type=int)
def inverse_number(x):
    _inverse_number(x)

def _inverse_number(x):
    """Display number x on screen."""
    display_image(Image.open('ledmatrix/number_inverse_{}.png'.format(x)).rotate(90))


def display_image(image):
    display.clear()
    draw = ImageDraw.Draw(image)
    display.set_image(image)
    display.write_display()

@cli.command()
@click.argument('iterations', type=int)
def loading_lokk(iterations):
    _loading_lokk(iterations)

def _loading_lokk(iterations):
    image_open = Image.open('ledmatrix/lokkit_icon_borderless.png').rotate(90)
    image_closed = Image.open('ledmatrix/lokkit_icon_borderless_closed.png').rotate(90)
    i = 0
    for x in xrange(iterations):
        display.clear()
        display.set_image(image_open if x % 2 == 0 else image_closed)
        display.write_display()
        time.sleep(0.5)

@cli.command()
@click.argument('iterations', type=int)
def loading_square_in(iterations):
    """Displays a loading square from outside to inside <iterations> times"""
    _loading_square_in(iterations)

def _loading_square_in(iterations):
    i = 0
    for f in xrange(iterations):
        for x in xrange(0, 4, 1):
            i = i % 3
            if i == 0:
                col = (255, 0, 0)
            elif i == 1:
                col = (255, 255, 0)
            elif i == 2:
                col = (0, 255, 0)
            i += 1
            image = Image.new('RGB', (8, 8))
            draw = ImageDraw.Draw(image)
            display.clear()
            draw.rectangle((x, x, 7-x, 7-x), outline=col, fill=(0, 0, 0))
            display.set_image(image)
            display.write_display()
            time.sleep(0.1)
    display.clear()
    display.write_display()

@cli.command()
def lokk_open():
    display_image(Image.open('ledmatrix/lokkit_icon_borderless.png').rotate(90))

@cli.command()
def lokk_closed():
    display_image(Image.open('ledmatrix/lokkit_icon_borderless_closed.png').rotate(90))

@cli.command()
def tick():
    _tick()

def _tick():
    image = Image.open('ledmatrix/tick.png').rotate(90)
    display.set_image(image)
    display.write_display()

@cli.command()
@click.argument('iterations', type=int)
def loading_square_out(iterations):
    """Displays a loading square from inside to outside <iterations> times"""
    _loading_square_out(iterations)

def _loading_square_out(iterations):
    i = 0
    for f in xrange(iterations):
        for x in xrange(3, -1, -1):
            i = i % 3
            if i == 0:
                col = (255, 0, 0)
            elif i == 1:
                col = (255, 255, 0)
            elif i == 2:
                col = (0, 255, 0)
            i += 1
            image = Image.new('RGB', (8, 8))
            draw = ImageDraw.Draw(image)
            display.clear()
            draw.rectangle((x, x, 7-x, 7-x), outline=col, fill=(0, 0, 0))
            display.set_image(image)
            display.write_display()
            time.sleep(0.1)
    display.clear()
    display.write_display()

def _loading_square(iterations):
    """Whole loading square with no duplicate writing"""
    i = 0
    for f in xrange(iterations):
        for x in xrange(1, 4, 1):
            i = i % 3
            if i == 0:
                col = (255, 0, 0)
            elif i == 1:
                col = (255, 255, 0)
            elif i == 2:
                col = (0, 255, 0)
            i += 1
            image = Image.new('RGB', (8, 8))
            draw = ImageDraw.Draw(image)
            display.clear()
            draw.rectangle((x, x, 7-x, 7-x), outline=col, fill=(0, 0, 0))
            display.set_image(image)
            display.write_display()
            time.sleep(0.1)
        display.clear()
        display.write_display()
        for x in xrange(2, -1, -1):
            i = i % 3
            if i == 0:
                col = (255, 0, 0)
            elif i == 1:
                col = (255, 255, 0)
            elif i == 2:
                col = (0, 255, 0)
            i += 1
            image = Image.new('RGB', (8, 8))
            draw = ImageDraw.Draw(image)
            display.clear()
            draw.rectangle((x, x, 7-x, 7-x), outline=col, fill=(0, 0, 0))
            display.set_image(image)
            display.write_display()
            time.sleep(0.1)
    display.clear()
    display.write_display()

@cli.command()
@click.argument('iterations', type=int)
def loading_square(iterations):
    """Displays a loading square from outside to inside <iterations> times"""
    _loading_square(iterations)


@cli.command()
@click.argument('color')
def fill(color):
    _fill(color)

def _fill(color):
    """Displays a filled image"""
    if color == 'red':
        col = (255, 0, 0)
    elif color == 'yellow':
        col = (255, 255, 0)
    elif color == 'green':
        col = (0, 255, 0)
    else:
        col = (0,0,0)
    image = Image.new('RGB', (8, 8))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 7, 7), outline=col, fill=col)
    display.set_image(image)
    display.write_display()
    display.clear()
    display.write_display()

@cli.command()
@click.argument('num', type=int)
def tx_received(num):
    """Some flashy thing when a tx has been received"""
    _tx_received(num)

def _tx_received(num):
    for x in xrange(3):
        _loading_square_in(1)
        _loading_square_out(1)
    _number(num)

@cli.command()
@click.argument('num', type=int)
def lock_unlock_received(num):
    _lock_unlock_received(num)

def _lock_unlock_received(num):
    _loading_lokk(8)
    _number(num)

@cli.command()
def progress():
    """Display progress on on screen."""
    click.echo('Displaying number %s!' % number)

@cli.command()
def logo():
    """Display lokkit logo on screen."""
    click.echo('Displaying number %s!' % number)

@cli.command()
def clear():
    """Clears the display"""
    display.clear()
    display.write_display()

@cli.command()
def test():
    """Test screen."""
    # Run through each color and pixel.
    # Iterate through all colors.
    for c in [BicolorMatrix8x8.RED, BicolorMatrix8x8.GREEN, BicolorMatrix8x8.YELLOW]:
        # Iterate through all positions x and y.
        for x in range(8):
            for y in range(8):
                # Clear the display buffer.
                display.clear()
                # Set pixel at position i, j to appropriate color.
                display.set_pixel(x, y, c)
                # Write the display buffer to the hardware.  This must be called to
                # update the actual display LEDs.
                display.write_display()
                # Delay for a quarter second.
                time.sleep(0.25)

    # Draw some colored shapes using the Python Imaging Library.

    # Clear the display buffer.
    display.clear()

    # First create an 8x8 RGB image.
    image = Image.new('RGB', (8, 8))

    # Then create a draw instance.
    draw = ImageDraw.Draw(image)

    # Draw a filled yellow rectangle with red outline.
    draw.rectangle((0, 0, 7, 7), outline=(255, 0, 0), fill=(255, 255, 0))

    # Draw an X with two green lines.
    draw.line((1, 1, 6, 6), fill=(0, 255, 0))
    draw.line((1, 6, 6, 1), fill=(0, 255, 0))

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


if __name__ == "__main__":
    cli()
