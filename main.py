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

# Задаём параметры цели (используемая картинка должна быть с такими же параметрами длины и ширины)
target_width = 80
target_height = 80

# Задаём координаты для перемещения цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Очки
score = 0
font = pygame.font.Font(None, 36)

# Создание игрового цикла
running = True
while running:
    screen.fill(color)
    #Функция для перебора событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Координаты мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверка попадания мыши в цель
            if mouse_x >= target_x and mouse_x <= target_x + target_width and mouse_y >= target_y and mouse_y <= target_y + target_height:
                # Перемещение цели
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                # Увеличение счета при попадании цели
                score += 1

# Отрисовка цели
    screen.blit(target, (target_x, target_y))

    # Отображение очков
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.update()

# Завершение игры (как только завершится цикл)
pygame.quit()