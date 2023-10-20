import random
import subprocess
import sys
import os

import pynput.mouse
from PIL import ImageGrab
from pynput.mouse import Listener
from fpdf import FPDF

x_coordinates = []
y_coordinates = []


def on_click(x, y, button, pressed):
    if button is pynput.mouse.Button.middle:
        if pressed:
            x_coordinates.append(int(x))
            y_coordinates.append(int(y))
        if not pressed:
            x_coordinates.append(int(x))
            y_coordinates.append(int(y))
            return False


def take_screenshot():
    with Listener(
            on_click=on_click
    ) as listener: listener.join()

    region = (min(x_coordinates), min(y_coordinates), max(x_coordinates), max(y_coordinates))
    screenshot = ImageGrab.grab(region)
    gray_img = screenshot.convert("L")
    filename = "TempImage.png"
    gray_img.save(filename)
    return filename


def create_pdf(image_filename, pdf_filename):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    page_width_mm = 190
    pdf.image(image_filename, x=10, w=page_width_mm)

    pdf.output(pdf_filename)

    os.remove(image_filename)


def put_on_remarkable(name):
    # TODO put at special location?
    # TODO make sure, filename does not yet exist, maybe pass as input?
    args = ("/Users/fluffyoctopus/dev/rmapi/rmapi", "put", name)
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    return output


if __name__ == '__main__':
    image = take_screenshot()
    filename = "file" + str(random.randint(0,42))
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    pdf_filename = filename + '.pdf'
    create_pdf(image, pdf_filename)
    output = put_on_remarkable(pdf_filename)
    os.remove(pdf_filename)
    print(output)
    # TODO maybe take several screenshots? put in same document? --> How to finish? (evtl timer?)

# https://blog.aspose.com/pdf/create-pdf-files-in-python/
# https://github.com/juruen/rmapi
# https://github.com/subutux/rmapy/blob/master/docs/source/quickstart.rst
