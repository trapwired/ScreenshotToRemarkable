import random
import subprocess
import sys
import os

import pynput.mouse
from PIL import ImageGrab
from pynput.mouse import Listener
from fpdf import FPDF

RMAPI_EXEC_PATH = "/Users/fluffyoctopus/dev/rmapi/rmapi"

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
    ) as listener:
        listener.join()

    region = (min(x_coordinates), min(y_coordinates), max(x_coordinates), max(y_coordinates))
    screenshot = ImageGrab.grab(region)
    gray_img = screenshot.convert("L")
    image_filename = "TempImage.png"
    gray_img.save(image_filename)
    return image_filename


def get_pdf_filename():
    filename = "file" + str(random.randint(0, 42))
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    pdf_filename = filename + '.pdf'
    return pdf_filename


def create_pdf(image_filename, pdf_filename):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    page_width_mm = 190
    pdf.image(image_filename, x=10, w=page_width_mm)

    pdf.output(pdf_filename)


def put_on_remarkable(name):
    args = (RMAPI_EXEC_PATH, "put", name)
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print(output)


def delete_temp_files(image_filename, pdf_filename):
    os.remove(image_filename)
    os.remove(pdf_filename)


if __name__ == '__main__':
    image = take_screenshot()
    pdf_filename = get_pdf_filename()
    create_pdf(image, pdf_filename)
    put_on_remarkable(pdf_filename)
    delete_temp_files(image, pdf_filename)
