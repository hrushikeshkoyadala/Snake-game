import pygame, random
from sounds import *
from pygame.locals import *


screen = pygame.display.set_mode((500, 500))
pygame.init()
FPS = 24
refresh = pygame.time.Clock()
score = 0
condition = True
prev_button = -1
button = -1


#Snake
class Snake:
    snake_head = [250, 250]
    snake_position = [[250, 250]]
    snake_color = [255, 255, 255]
    def display_snake(self):
        for position in self.snake_position:
            pygame.draw.rect(screen, self.snake_color, pygame.Rect(position[0], position[1], 10, 10))

#Apple
class Apple:
    apple_position = [random.randrange(1, 50)*10, random.randrange(1, 50)*10]
    apple_image = pygame.image.load('apple.png')
    def display_apple(self):
        screen.blit(self.apple_image, self.apple_position)



#Displays final score
def display_final_score():
    global score, screen, refresh
    display_text = "Score = " + str(score)
    largeText = pygame.font.Font('freesansbold.ttf', 35)
    game_over = largeText.render("Game Over", True, (0, 0, 255))
    TextSurf = largeText.render(display_text, True, (0, 0, 255))
    TextRect = TextSurf.get_rect()
    TextRect.center = (250, 250)
    screen.blit(TextSurf, TextRect)
    screen.blit(game_over, (160, 180))
    pygame.display.update()
    while (1):
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                exit(0)
            elif event.type == QUIT:
                exit(0)




#Initializes
def initialize():
    screen.fill((0, 0, 0)) #Setting BG color
    pygame.display.set_caption('Snake')
    pygame.display.flip()


def collision_with_wall(s):
    if (s.snake_head[0] >= 500 or s.snake_head[0] < 0 or s.snake_head[1] >= 500 or s.snake_head[1] < 0):
        return True
    return False


def collision_with_snake(s):
    if (s.snake_head in s.snake_position[1:]):
        return True
    return False



def eats_apple(s, a):
    for i in s.snake_position:
        if i[0] == a.apple_position[0] and i[1] == a.apple_position[1]:
            return True
    return False



initialize()
snake = Snake()
apple = Apple()

while condition:
    prev_button = button
    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == pygame.K_LEFT and prev_button != 1:
                button = 0

            elif event.key == pygame.K_RIGHT and prev_button != 0:
                button = 1

            elif event.key == pygame.K_DOWN and prev_button != 3:
                button = 2

            elif event.key == pygame.K_UP and prev_button != 2:
                button = 3

            elif event.key == K_ESCAPE:
                exit(0)

        elif event.type == QUIT:
            exit(0)

    if button == 1:
        snake.snake_head[0] += 10

    elif button == 0:
        snake.snake_head[0] -= 10

    elif button == 2:
        snake.snake_head[1] += 10

    elif button == 3:
        snake.snake_head[1] -= 10



    if collision_with_wall(snake) or collision_with_snake(snake):
        play_sound_2()
        screen.fill((0, 0, 0))
        display_final_score()
        exit(0)

    elif eats_apple(snake, apple):
        FPS += 1
        play_sound_1()
        snake.snake_position.insert(0, apple.apple_position)
        score += 1
        apple.apple_position = [random.randrange(1, 50)*10, random.randrange(1, 50)*10]

    else:
        if (prev_button != button):
            play_sound_3()
        snake.snake_position.insert(0, snake.snake_head[:])
        snake.snake_position.pop()

    screen.fill((0, 0, 0))
    snake.display_snake()
    apple.display_apple()

    #Refresh rate
    refresh.tick(FPS)
    pygame.display.flip()

pygame.quit()
