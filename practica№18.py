#Задание 1
from PIL import Image

image = Image.open("D:\\screenshot.jpg")
baw = image.convert("L")
baw.save("screenshot_bw.jpg.")
baw.show()
#Задание 2
from PIL import Image

image = Image.open("D:\\screen_camera.png")
rot = image.rotate(180)
rot.save("screen_camera.png")
rot.show()
#Задание 3
from PIL import Image

image = Image.open("D:\\figures.png")
cube = image.crop((265,115,485,400))
cube.save("cube.png")
cube.show()
#Задание 4
from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (200, 200), "green")
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", 20)
draw.text((24, 50), "Hol was here", fill="white", font=font)
image.save("Hol was here.png")
image.show()
#Задание 5
from PIL import Image, ImageDraw

image = Image.open("D:\\pixels.png")
draw = ImageDraw.Draw(image)
draw.rectangle((178,35,221,80), outline="red")
draw1 = ImageDraw.Draw(image)
draw1.rectangle((22,150,51,229), outline="blue")
image.save("pixels_ready.png")
image.show()
#Задание 6
from PIL import Image, ImageDraw

pixels = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 1, 1, 1, 1, 1, 0, 1],
 [1, 1, 1, 0, 0, 0, 1, 1, 1],
 [1, 1, 0, 1, 0, 1, 0, 1, 1],
 [1, 1, 0, 0, 1, 0, 0, 1, 1],
 [1, 1, 0, 1, 0, 1, 0, 1, 1],
 [1, 1, 1, 0, 0, 0, 1, 1, 1],
 [1, 0, 1, 1, 1, 1, 1, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1]]

image = Image.new("RGB", (9,9), "white")
draw = ImageDraw.Draw(image)
for y, row in enumerate(pixels):
    for x, pixel in enumerate(row):
        if pixel == 1:
            color = "black"
        else:
            color = "white"
        draw.rectangle((x,y,x,y), fill = color)
image.save("my pixel pict.png")
image.show()
