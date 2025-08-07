import pygame
import random
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True

COLORS = {
    "rock": (200, 0, 0),
    "paper": (0, 200, 0),
    "scissors": (0, 0, 200)
}

# Da RULES
RULES = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}


class Object:
    def __init__(self, kind):
        self.kind = kind
        self.radius = 10
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)
        self.dx = random.choice([-3, 3])
        self.dy = random.choice([-3, 3])
        self.alive = True
    
    def move(self):
        self.x += self.dx
        self.y += self.dy

        #bounce on edges
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.dx *= -1
        if self.y <= self.radius or self.y >= HEIGHT - self.radius:
            self.dy *= -1
    
    def draw(self, screen):
        if self.alive:
            if self.kind == "rock":
                pygame.draw.circle(screen, COLORS[self.kind], (int(self.x), int(self.y)), self.radius)
            elif self.kind == "paper":
                pygame.draw.circle(screen, COLORS[self.kind], (int(self.x), int(self.y)), self.radius)
            elif self.kind == "scissors":
                pygame.draw.circle(screen, COLORS[self.kind], (int(self.x), int(self.y)), self.radius)
            
    def collision(self, other):
        if not self.alive or not other.alive:
            return
        dist = math.hypot(self.x - other.x, self.y - other.y)
        if dist < self.radius + other.radius:
            if RULES[self.kind] == other.kind:
                other.kind = self.kind
            elif RULES[other.kind] == self.kind:
                self.kind = other.kind

def create_objects():        
    objects = []
    for _ in range(5):
        objects.append(Object("rock"))
        objects.append(Object("paper"))
        objects.append(Object("scissors"))
    return objects

#Game Loop
objects = create_objects()
running = True 
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = false
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                objects = create_objects()

    for obj in objects:
        obj.move()
        obj.draw(screen)

    for i in range(len(objects)):
        for j in range(i + 1, len(objects)):
            objects[i].collision(objects[j])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

