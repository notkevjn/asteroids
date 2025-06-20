import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon (screen, (255,255,255), self.triangle(), 2)

    def update(self, dt):
        pass


    def collision (self, object):
        distance = pygame.math.Vector2.distance_to(object.position, self.position)
        radius_both = self.radius + object.radius

        if distance <= radius_both:
            return True
        else:
            return False