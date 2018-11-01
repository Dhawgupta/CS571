import pygame

(width, height) = (300,200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tutorial = 1")
background_colour = (255,255,255)
clock = pygame.time.Clock()
crashed = False
screen.fill(background_colour)
pygame.draw.circle(screen, (0,0,255), (150, 50), 15, 1)
running = True
while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()

