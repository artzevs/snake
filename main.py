import pygame
import sys, os, random
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.body = []
        for i in range(3):
            self.body.append(Vector2(cell_number / 2 - i, cell_number / 2))
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        head = self.body[0]
        head_rect = pygame.Rect(head.x * cell_size, head.y * cell_size,
                                cell_size, cell_size)
        pygame.draw.rect(screen, pygame.Color('Green'), head_rect)
        # screen.blit(corgi, head_rect)
        for block in self.body[1:]:
            block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size,
                                     cell_size, cell_size)
            # pygame.draw.rect(screen, pygame.Color('Green'), block_rect)
            screen.blit(corgi, block_rect)

    def move_snake(self):
        """movement of each block of snake"""
        body_copy = self.body[:-1]
        head_position = Vector2((body_copy[0].x + self.direction.x) % cell_number,
                                (body_copy[0].y + self.direction.y) % cell_number)
        body_copy.insert(0, head_position)
        self.body = body_copy

    def add_block(self):
        """snake increase"""
        self.body.append(self.body[-1] - self.direction)


class Fruit:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size,
                                 cell_size, cell_size)
        screen.blit(corgi, fruit_rect)
        # pygame.draw.rect(screen, pygame.Color('Red'), fruit_rect)


class Main:
    """Logic of the game"""

    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_fruit_collision()
        self.check_snake_collision()


    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_fruit_collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.snake.add_block()
            self.fruit = Fruit()
        if self.fruit.position in self.snake.body:
            self.fruit = Fruit()

    def check_snake_collision(self):
        if self.snake.body[0] in self.snake.body[1:]:
            self.snake = Snake()

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, pygame.Color('black'))
        score_position = (cell_size * cell_number - 60, cell_size * 2 - 40)
        score_rect = score_surface.get_rect(center=(score_position))
        screen.blit(score_surface, score_rect)


pygame.init()

cell_size = 40
cell_number = 20

direction_up = Vector2(0, -1)
direction_down = Vector2(0, 1)
direction_left = Vector2(-1, 0)
direction_right = Vector2(1, 0)

game_font = pygame.font.Font('20179.ttf', 50)

screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

corgi = pygame.image.load('fruit(corgi).png').convert_alpha()
corgi = pygame.transform.scale(corgi, (cell_size + 4, cell_size + 4))

main_game = Main()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) \
                    and main_game.snake.direction != (-direction_up):
                main_game.snake.direction = direction_up

            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) \
                    and main_game.snake.direction != (-direction_down):
                main_game.snake.direction = direction_down

            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) \
                    and main_game.snake.direction != (-direction_right):
                main_game.snake.direction = direction_right

            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) \
                    and main_game.snake.direction != (-direction_left):
                main_game.snake.direction = direction_left

    screen.fill(pygame.Color('Blue'))

    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
