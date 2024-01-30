import pygame
import os
import numpy as np
from PIL import Image
import sys
# python3 gglit.py запуск программы

pygame.init()
screen_width = 900
screen_height = 600
fps = 60
background_color = (255, 255, 255) # изменение цвета фона на белый
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Простой рисовальщик")
brush_size = 100
brush_color = (0, 0, 0) # изменение цвета кисти на черный
drawing = False
count = 1
mous = 0
directory = "." # Update this path to match your actual directory
if not os.path.exists(directory):
    os.makedirs(directory)

# определяем начальные значения previous_x и previous_y
previous_x = screen_width // 2
previous_y = screen_height // 2
current_x, current_y = pygame.mouse.get_pos()

i = 1
running = True
while running:
    pygame.time.Clock().tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and drawing:
            mous = 1

        if event.type == pygame.QUIT:
            running = False

        # в цикле обработки событий
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.key.get_mods() & pygame.KMOD_CTRL:
            drawing = True
            brush_size = 100
            pygame.draw.line(screen, brush_color, event.pos, event.pos, brush_size)
            previous_x, previous_y = event.pos

        if event.type == pygame.MOUSEMOTION and drawing:
            current_x, current_y = pygame.mouse.get_pos()

            # вычисляем расстояние между точками
            distance = ((current_x - previous_x) ** 2 + (current_y - previous_y) ** 2) ** 0.5

            # задаем новый размер кисти в зависимости от расстояния
            brush_size = int(max(30, brush_size - distance / 10))

            # рисуем линию между предыдущей и текущей точками
            pygame.draw.line(screen, brush_color, (previous_x, previous_y), (current_x, current_y), brush_size)

            # обновляем предыдущие координаты
            previous_x, previous_y = current_x, current_y


        # конвертируйте и нормализуйте сохраненные изображения
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and drawing:
            drawing = False
            image_path = os.path.join(directory, f'{count}-2.png')
            pygame.image.save(screen, image_path)
            image = Image.open(image_path).convert('L')  # convert to grayscale
            image = image.resize((28, 28))  # resize to 28x28 pixels
            image_array = np.array(image)
            image = Image.fromarray(image_array).convert('L')  # normalize and invert colors (black on white)
            image.save(image_path)
            count += 1
            mous = 0
            brush_size = 20

        if event.type == pygame.MOUSEBUTTONDOWN and mous == 0:
            screen.fill(background_color)

     #   if event.type == pygame.KEYUP and event.key == pygame.K_LCTRL:
     #       # Отпущена кнопка Ctrl, заканчиваем рисование
    #        pygame.quit()
    #        sys.exit()

    pygame.display.flip()

pygame.quit()
