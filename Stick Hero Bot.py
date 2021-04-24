#!/usr/bin/env python3

from ppadb.client import Client
from PIL import Image
import numpy
import time

adb = Client("127.0.0.1")
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

while True:
    image = device.screencap()

    with open('screen.png', 'wb') as f:
        f.write(image)

    image = Image.open('screen.png')
    image = numpy.array(image, dtype=numpy.uint8)
    pixels = [list(i[:3]) for i in image[1350]]
    transitions = []
    ignore = True
    black = True

    for i, pixel in enumerate(pixels):
        r, g, b = [int(i) for i in pixel]

        if ignore and (r+g+b) != 0:
            continue

        ignore = False

        if black and (r+g+b) != 0:
            black = not black
            transitions.append(i)
            continue

        if not black and (r+g+b) == 0:
            black = not black
            transitions.append(i)
            continue

    start, target1, target2 = transitions


    # gap = (target1 - start)+5
    gap = (target1 - start) - 7
    # target = target2
    target = ((target2 - target1)/2)
    # distance = (gap)
    distance = (gap + target)

    print(f'transition points: {transitions}, distance: {distance}')

    device.shell(f'input touchscreen swipe 500 500 500 500 {int(distance)}')

    time.sleep(3)
