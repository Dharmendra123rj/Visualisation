import pygame

HEIGHT = 1200
WIDTH = 800
WIN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('pixel visualisation')


class Node:
    def __init__(self, row, col, width, color):
        self.x = row * width
        self.y = col * width
        self.width = width
        self.color = color

    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.width))
        pygame.display.update()





def main():
    Grid = []
    n = 0
    for i in range(400):
        Grid.append([])
        for j in range(600):
            itr = n
            b = itr % 256
            itr //= 256
            g = itr % 256
            itr //= 256
            r = itr % 256
            Grid[i].append(Node(j, i, 2, (r, g, b)))
            n += 1
    
    for each in Grid:
        for node in each:
            node.draw()
            
                 
if __name__ == "__main__":
    main()


