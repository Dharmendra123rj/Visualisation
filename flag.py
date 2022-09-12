import pygame

HEIGHT = 1200
WIDTH = 700
WIN  = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('National Flag')

ORANGE = (255, 170, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Node:
    def __init__(self, row, col, width, color):
        self.row = row
        self.col = col
        self.width = width
        self.x = row * width
        self.y = col * width
        self.color = color
    
    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), 5)
    


def fill_node(width):
    Grid = []
    for i in range(WIDTH//width):
        Grid.append([])
        for j in range(HEIGHT//width):
            Grid[i].append(Node(j, i, width, WHITE))
    
    return Grid

   

def main():
    width = 20
    Grid = fill_node(width)
    clk = pygame.time.Clock()
    
    div = WIDTH // width // 3
    for i in range(10, 15):
        for j in range(20, 45):
            Grid[i][j].color = ORANGE
            Grid[i][j].draw()
            pygame.display.update()
            clk.tick(50)
    
    for i in range(15, 20):
        for j in range(20, 45):
            if(j>29 and j<35):
                Grid[i][j].color = BLUE
                Grid[i][j].draw()
                pygame.display.update()
                clk.tick(20)
                continue
            Grid[i][j].color = WHITE
            Grid[i][j].draw()
            pygame.display.update()
            clk.tick(50)
    
    for i in range(20, 25):
        for j in range(20, 45):
            Grid[i][j].color = GREEN
            Grid[i][j].draw()
            pygame.display.update()
            clk.tick(50)
    
                
                
                
        
main()