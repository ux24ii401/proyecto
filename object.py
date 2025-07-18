import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, pos, size, image_directory, group):
        super().__init__(group)

        self.pos = pos
        self.size = size
        self.image_directory = image_directory

        self.setImage()  # Se llama al inicio para que tenga imagen desde el primer frame

    def setImage(self):
        # Cargar imagen
        image = pygame.image.load(self.image_directory).convert_alpha()
        # Escalar al tamaño deseado
        self.image = pygame.transform.scale(image, self.size)
        # Establecer rectángulo para ubicar en pantalla
        self.rect = self.image.get_rect(topleft=self.pos)

    def update(self):
        self.setImage()
