import sys, pygame
pygame.init()

size = width, height = 480, 476
screen = pygame.display.set_mode(size)
background = pygame.image.load('taulell.bmp').convert()
screen.blit(background, (0, 0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
	
    pygame.display.update()
    pygame.time.delay(100)

