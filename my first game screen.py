import pygame
pygame.init()
white = (255, 255, 255)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((900,900))

pygame.display.set_caption('Image')

image = pygame.image.load('image.jpeg')

DEFAULT_IMAGE_SIZE = (500,500)

image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

DEFAULT_IMAGE_POSITION = (200,200)


while True:
    
    screen.fill(white)
    screen.blit(image, DEFAULT_IMAGE_POSITION)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            pygame.quit()
            quit()
            
            
            
    pygame.display.flip()
    clock.tick(30)