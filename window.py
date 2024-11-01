import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))

colour = (100, 0, 198)
screen.fill(colour)

done = False

while not done:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.display.flip()