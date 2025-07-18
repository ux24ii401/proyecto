import pygame, sys, random
from object import *
from frog import *
from lane import *

class Game:
    def __init__(self, screen_dimensions, screen_caption, screen_color):
        pygame.init()
        pygame.display.set_mode(screen_dimensions)
        pygame.display.set_caption(screen_caption)

        self.screen_color = screen_color
        self.DISPLAY = pygame.display.get_surface()

        # Grupos de sprites
        self.object_group = pygame.sprite.Group()
        self.car_group = pygame.sprite.Group()
        self.river_group = pygame.sprite.Group()
        self.frog_group = pygame.sprite.Group()

        self.all_groups = [
            self.object_group,
            self.car_group,
            self.river_group,
            self.frog_group
        ]

        self.river_speeds = {}
        self.assetSetup()

    def assetSetup(self):
        # Fondo
        Object((0, 0), (672, 768), "assets/background.png", self.object_group)

        # Grass rojo (inicio y fin)
        for x in range(14):
            Object((x * 48, 384), (48, 48), "assets/grass/red.png", self.object_group)
            Object((x * 48, 672), (48, 48), "assets/grass/red.png", self.object_group)

        # Grass verde (en el medio superior)
        for x in range(28):
            Object((x * 24, 72), (24, 72), "assets/grass/green.png", self.object_group)

        #lanes
        speeds = [-1.25, -1, -0.75, -0.5, -0.25, 0.5, 0.75, 1, 1.25, 1.5]

        random.shuffle(speeds)

        #river lanes
        for y in range(5):
            y_pos = y*48 + 144
            new_lane = Lane((0, y_pos), self.river_group, speeds.pop(), "river")
            self.river_speeds[y_pos // 48] = new_lane.speed

        #street lanes
        for y in range(5):
            y_pos = y*48 + 432
            Lane((0, y_pos), self.car_group, speeds.pop(), "street")


        # Rana
        self.frog = Frog((336, 672), (48, 48), "assets/frog/up.png", self.frog_group, [self.car_group, self.river_group], self.river_speeds)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.frog.keyups = []

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYUP:
                    self.frog.keyups.append(event.key)

            # Actualizar y dibujar todos los grupos
            for group in self.all_groups:
                for sprite in group:
                    sprite.update()
                group.draw(self.DISPLAY)

            pygame.display.update()
            clock.tick(60)  # Limita a 60 FPS

# Crear el juego
if __name__ == "__main__":
    game = Game((672, 768), "Frogger!!", (0, 0, 0))
    game.run()
