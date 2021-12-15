import os
import random
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
    size = width, height = (300,) * 2
    pygame.display.set_caption("Герой двигается!")
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color("white"))

    fps = 60  # количество кадров в секунду
    clock = pygame.time.Clock()
    running = True

    class Sprite(pygame.sprite.Sprite):
        image = load_image("creature.png")

        def __init__(self, *group):
            super().__init__(*group)
            self.image = Sprite.image
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 0

        def update(self, *args):
            if args and args[0].type == pygame.KEYUP:
                if args[0].key == pygame.K_LEFT:
                    self.rect.x -= 10
                elif args[0].key == pygame.K_RIGHT:
                    self.rect.x += 10
                elif args[0].key == pygame.K_DOWN:
                    self.rect.y += 10
                elif args[0].key == pygame.K_UP:
                    self.rect.y -= 10

    all_sprites = pygame.sprite.Group()
    Sprite(all_sprites)
    all_sprites.draw(screen)

    while running:  # главный игровой цикл
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                all_sprites.update(event)

        screen.fill(pygame.Color("white"))
        all_sprites.draw(screen)
        pygame.display.flip()  # смена кадра
        # временная задержка
        clock.tick(fps)
