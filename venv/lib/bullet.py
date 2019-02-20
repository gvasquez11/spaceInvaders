import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object, at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create bullet rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top - 10

        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


class AlienBullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen):
        """Create a bullet object, at the ship's current position."""
        super(AlienBullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, ai_settings.bullet_height)
        self.y = float(self.rect.y)
        self.color = (255, 0, 0)
        self.speed_factor = ai_settings.alien_bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y += self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
