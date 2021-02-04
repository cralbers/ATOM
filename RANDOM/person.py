from sense_hat import sense_hat
from time import sleep

sense = SenseHat()

b = (44, 129, 178)
p = (178, 44, 80)
g = (50, 119, 50)
w = (150, 150, 150)

person = [
g, g, g, g, g, g, g, g,
g, g, g, g, g, g, g, g,
w, w, w, g, g, w, w, w,
b, w, w, g, g, b, w, w,
w, w, w, g, g, w, w, w,
g, g, g, g, g, g, g, g,
g, g, p, p, p, p, g, g,
g, g, g, g, g, g, g, g
]

sense.set_pixels(image)

while True:
    sleep(1)
    sense.flip_h
