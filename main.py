import pygame
import random

pygame.init()

# Создание игрового окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Функция для создания игрового экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Задаём название игрового окна
pygame.display.set_caption("Игра тир")

# Создаём иконку экрана
icon = pygame.image.load("img/тир.jpg")
# Устанавливаем иконку
pygame.display.set_icon(icon)

# Создание "цели" в игре тир
target = pygame.image.load("img/cake.png")

# Задаём параметры цели
target_width = 80
target_height = 80

# Задаём координаты для перемещения цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



# Создание игрового цикла
running = True
while running:
    pass

# Завершение игры (как только завершится цикл)
pygame.quit()