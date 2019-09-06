import pygame
from pygame.locals import *
import sys

# set up pygame
pygame.init()

# set up the window
window = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('hello world!')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up the fonts
font = pygame.font.SysFont(None, 48)

# set up the text
text = font.render('Hello world!', True, WHITE, BLUE)
text_rect = text.get_rect()
text_rect.centerx = window.get_rect().centerx
text_rect.centery = window.get_rect().centery

# draw the white backkground onto the surface
window.fill(WHITE)

# draw a green polygon onto the surface
pygame.draw.polygon(window, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# draw some blue lines onto the surface
pygame.draw.line(window, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(window, BLUE, (120, 60), (60, 120))
pygame.draw.line(window, BLUE, (60, 120), (120, 120), 4)

# draw a blue curcle onto the sruface
pygame.draw.circle(window, BLUE, (300, 50), 20, 0)

# draw a red ellipse onto the surface
pygame.draw.ellipse(window, RED, (300, 250, 40, 80), 1)

# draw the text's background rectagle onto the surface
pygame.draw.rect(window, RED, (text_rect.left - 20, text_rect.top - 2, text_rect.width + 40, text_rect.height + 40))

# get a pixel array of the sruface
pixel_array = pygame.PixelArray(window)
pixel_array[480][380] = BLACK
del pixel_array

# draw the text onto the sruface
window.blit(text, text_rect)

# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
