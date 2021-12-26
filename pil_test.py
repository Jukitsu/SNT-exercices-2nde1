from PIL import Image
from random import *
WIDTH = 1800
HEIGHT = 950

im = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0))

def pgcd(a, b):
    return pgcd(b, a%b) if b else abs(a)  # recursive hack

def irreductible_frac(frac):
    p, q = frac
    a = pgcd(p, q)
    return (p // a, q // a)

def pixel2i(coords, rgb=(255, 255, 255)):
    im.putpixel(coords, rgb)

def sky_stars(n, rand=False):
    for k in range(n):
        x, y = randrange(0, WIDTH), randrange(0, HEIGHT)
        rgb = (randrange(75, 256), randrange(150, 256), randrange(50, 256)) if rand else (255, 255, 255)
        pixel2i((x, y), rgb)

def line2p(p1, p2, rgb=(255, 255, 255)):
    x1, y1 = p1
    x2, y2 = p2
    dy = y2 - y1
    dx = x2 - x1
    if abs(dy) < abs(dx):
        xstep = 2 * (x2 > x1) - 1    
        for x in range(x1, x2 + xstep, xstep):
            y = y1 + (x - x1) * dy//dx
            pixel2i((x, y), rgb)
    elif dy != 0:
        ystep = 2 * (y2 > y1) - 1
        for y in range(y1, y2 + ystep, ystep):
            x = x1 + (y - y1) * dx//dy
            pixel2i((x, y), rgb)
    
        

def triangle3p(vertex1, vertex2, vertex3, rgb=(255, 255, 255)):
    line2p(vertex1, vertex2, rgb)
    line2p(vertex2, vertex3, rgb)
    line2p(vertex3, vertex1, rgb)


def rectangle2p(p1, p2, rgb=(255, 255, 255)):
    x1, y1 = p1
    x2, y2 = p2
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            pixel2i((x, y), rgb)

def circle1p1f(center, radius, rgb=(255, 255, 255)):
    xo, yo = center
    for x in range(100 * radius // 100 + 1):
        y = radius
        while x*x + y*y > radius*radius:
            y-=1
        pixel2i((xo + x, yo + y), rgb)
        pixel2i((xo - x, yo + y), rgb)
        pixel2i((xo + x, yo - y), rgb)
        pixel2i((xo - x, yo - y), rgb)
        pixel2i((xo + y, yo + x), rgb)
        pixel2i((xo - y, yo + x), rgb)
        pixel2i((xo + y, yo - x), rgb)
        pixel2i((xo - y, yo - x), rgb)

def disk1p1f(center, radius, rgb=(255, 255, 255)):
    xo, yo = center
    for x in range(100 * radius // 100 + 1):
        y = radius
        while x*x + y*y > radius*radius:
            y-=1
        for t in range(x, y+1):
            pixel2i((xo + x, yo + t), rgb)
            pixel2i((xo + t, yo + x), rgb)
            pixel2i((xo - x, yo + t), rgb)
            pixel2i((xo - t, yo + x), rgb)
            pixel2i((xo + x, yo - t), rgb)
            pixel2i((xo + t, yo - x), rgb)
            pixel2i((xo - x, yo - t), rgb)
            pixel2i((xo - t, yo - x), rgb)

sky_stars(10000)

for i in range(0, 10):
    disk1p1f((randint(0, WIDTH-1), randint(0, HEIGHT-1)),
            randint(0, 100),
            rgb=(randint(0, 255), randint(0, 255), randint(0, 255)))


im.show()
