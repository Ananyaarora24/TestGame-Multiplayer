import pygame
from network import Network

w= 800
h = 700

display = pygame.display.set_mode((w,h))

pygame.display.set_caption("Client")

Number_client = 0

class Player():
    def __init__(self, a, b, w, h, color):
        self.a = a
        self.b = b
        self.w = w
        self.h = h
        self.color = color
        self.rect = pygame.Rect(a,b,w,h)
        self.val = 4

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.a -= self.val
        
        if keys[pygame.K_RIGHT]:
            self.a += self.val

        if keys[pygame.K_UP]:
            self.b -= self.val

        if keys[pygame.K_DOWN]:
            self.b += self.val
        
        self.update()

    def update(self):
        self.rect = pygame.Rect(self.a,self.b,self.w,self.h)

def read_position(data_str): #string to tuple
    data_str = data_str.split(",")
    return int(data_str[0]),int(data_str[1])

def make_position(data_tup):#tuple to string
    return str(data_tup[0])+","+str(data_tup[1])
        


def redraw(display, player1, player2):
    display.fill((0,0,0))
    player1.draw(display)
    player2.draw(display)
    pygame.display.update()


def main():
    run = True
    net=Network()
    startPos = read_position(net.get_position())
    p1 = Player(startPos[0],startPos[1],100,100,(255, 165, 0))
    p2 = Player(0,0,100,100,(128, 0, 128))
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2Position = read_position(net.send(make_position((p1.a,p1.b))))
        p2.a = p2Position[0]
        p2.b = p2Position[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.event.get():
                run = False
                pygame.quit()
        p1.move()
        redraw(display, p1, p2)

main()
            



