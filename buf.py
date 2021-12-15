import os
import sys
import pygame


def load_image(name, color_key=-1):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    size = width, height = (500,) * 2
    pygame.display.set_caption("Свой курсор мыши")
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))

    fps = 60  # количество кадров в секунду
    clock = pygame.time.Clock()
    running = True
    mouse_coords = [None,] * 2

    image = load_image("arrow.png")

    while running:  # главный игровой цикл
        screen.fill(pygame.Color("black"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse_coords = event.pos

        if mouse_coords[0] and pygame.mouse.get_focused():
            pygame.mouse.set_visible(False)
            screen.blit(image, tuple(mouse_coords))

        pygame.display.flip()  # смена кадра
        # временная задержка
        clock.tick(fps)
