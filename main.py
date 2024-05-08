import pygame

pygame.init()

# Создание игрового окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Функция для создания игрового экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Задаём название игрового окна
pygame.display.set_caption("Игра тир")

# Создаём иконку экрана
icon = pygame.image.load('icon.png')


# Создание игрового цикла
running = True
while running:
    pass

# Завершение игры (как только завершится цикл)
pygame.quit()