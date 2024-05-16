import classes, constants, pygame, sys

pygame.init()
screen = pygame.display.set_mode((constants.GRID_SIZE,constants.GRID_SIZE))
clock = pygame.time.Clock()

fruit = classes.FRUIT()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill((175,215,70))
    fruit.drawFruit(screen)
    pygame.display.update()
    clock.tick(60)