import pygame
from pygame.locals import *
import random

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("Snake And Apple Game")
clock = pygame.time.Clock()

SIZE = 40
WIDTH = 1500
HEIGHT = 800
BACKGROUND_COLOR = (0, 80, 50)

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("data/block.jpg").convert()
        self.x = [0]
        self.y = [0]
        self.length = 1
        self.direction = 'down'

    def move_left(self): self.direction = 'left'
    def move_right(self): self.direction = 'right'
    def move_up(self): self.direction = 'up'
    def move_down(self): self.direction = 'down'

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        elif self.direction == 'right':
            self.x[0] += SIZE
        elif self.direction == 'up':
            self.y[0] -= SIZE
        elif self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        self.parent_screen.fill(BACKGROUND_COLOR)
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("data/apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x = random.randint(0, (WIDTH - SIZE) // SIZE) * SIZE
        self.y = random.randint(0, (HEIGHT - SIZE) // SIZE) * SIZE

class ScoreCard:
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.SysFont('arial', 30)

    def draw(self, score):
        pygame.draw.rect(self.surface, (0, 0, 0), (WIDTH - 200, 10, 180, 40))
        text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        self.surface.blit(text, (WIDTH - 190, 15))

def is_collision(x1, y1, x2, y2):
    if x1 >= x2 and x1 < x2 + SIZE:
        if y1 >= y2 and y1 < y2 + SIZE:
            return True
    return False

def game_over(surface, score):
    font = pygame.font.SysFont('arial', 60)
    text = font.render(f"Game Over! Your Score: {score}", True, (255, 0, 0))
    surface.blit(text, (400, 400))
    pygame.display.flip()
    pygame.time.wait(3000)

snake = Snake(screen)
apple = Apple(screen)
scorecard = ScoreCard(screen)

MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_EVENT, 150)

running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                snake.move_left()
            elif event.key == K_RIGHT:
                snake.move_right()
            elif event.key == K_UP:
                snake.move_up()
            elif event.key == K_DOWN:
                snake.move_down()

        if event.type == MOVE_EVENT:
            snake.walk()

            if is_collision(snake.x[0], snake.y[0], apple.x, apple.y):
                snake.increase_length()
                apple.move()

            for i in range(1, snake.length):
                if is_collision(snake.x[0], snake.y[0], snake.x[i], snake.y[i]):
                    game_over(screen, snake.length)
                    running = False
                    break

            if snake.x[0] < 0 or snake.x[0] >= WIDTH or snake.y[0] < 0 or snake.y[0] >= HEIGHT:
                game_over(screen, snake.length)
                running = False

    snake.draw()
    apple.draw()
    scorecard.draw(snake.length)
    pygame.display.flip()

    clock.tick(120)
