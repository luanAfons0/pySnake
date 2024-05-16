import random, constants, pygame
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x = random.randint(0, constants.CELL_NUMBER - 1)
        self.y = random.randint(0, constants.CELL_NUMBER - 1)
        self.pos = Vector2(self.x,self.y)
        
    def drawFruit(self,screen):
        fruit_rect = pygame.Rect(
            int(self.pos.x * constants. CELL_SIZE),
            int(self.pos.y * constants.CELL_SIZE),
            constants.CELL_SIZE,
            constants.CELL_SIZE)
        pygame.draw.rect(screen,(255,0,0),fruit_rect)