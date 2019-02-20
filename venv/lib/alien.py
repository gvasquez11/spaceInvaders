import pygame
from pygame.sprite import Sprite
import math


class Alien1(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super(Alien1, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image, and set its rect attribute.
        self.images = []
        self.images.append(pygame.image.load('/Users/gregoryvasquez/PycharmProjects/spaceInvaders/images/alien1-1.png.png'))
        self.images.append(pygame.image.load('/Users/gregoryvasquez/PycharmProjects/spaceInvaders/images/alien1-2.png.png'))
        self.images.append(pygame.image.load('/Users/gregoryvasquez/PycharmProjects/spaceInvaders/images/Explosion1-1.png.png'))
        self.images.append(pygame.image.load('/Users/gregoryvasquez/PycharmProjects/spaceInvaders/images/Explosion1-2.png.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.boom = False
        self.score = 10

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

        self.index += .05
        if self.index >= 2 and not self.boom:
            self.index = 0
        if self.boom:
            if self.index < 2.5:
                self.index = 2.5
            if self.index >= 4:
                self.index = 0
                self.boom = False
                self.kill()
        self.image = self.images[math.floor(self.index)]

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)


class Alien2(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super(Alien2, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image, and set its rect attribute.
        self.images = []
        self.images.append(pygame.image.load('/Users/gregoryvasquez/PycharmProjects/spaceInvaders/images/alien2-1.png.png'))
        self.images.append(pygame.image.load('/Users/gregoryvasquez/PycharmProjects/spaceInvaders/images/alien2-2.png.png'))
        self.images.append(pygame.image.load('/Users/gregoryvasquez/PycharmProjects/spaceInvaders/images/Explosion1-1.png.png'))
        self.images.append(pygame.image.load('/Users/gregoryvasquez/PycharmProjects/spaceInvaders/images/Explosion1-2.png.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

        self.boom = False
        self.score = 20

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

        self.index += .05
        if self.index >= 2 and not self.boom:
            self.index = 0
        if self.boom:
            if self.index < 2.5:
                self.index = 2.5
            if self.index >= 4:
                self.index = 0
                self.boom = False
                self.kill()
        self.image = self.images[math.floor(self.index)]

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)


class Alien3(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super(Alien3, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image, and set its rect attribute.
        self.images = []
        self.images.append(pygame.image.load('/Users/gregoryvasquez/PycharmProjects/spaceInvaders/images/alien3-1.png.png'))
        self.images.append(pygame.image.load('/Users/gregoryvasquez/PycharmProjects/spaceInvaders/images/alien3-2.png.png'))
        self.images.append(pygame.image.load('/Users/gregoryvasquez/PycharmProjects/spaceInvaders/images/Explosion1-1.png.png'))
        self.images.append(pygame.image.load('/Users/gregoryvasquez/PycharmProjects/spaceInvaders/images/Explosion1-2.png.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

        self.boom = False
        self.score = 40

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

        self.index += .05
        if self.index >= 2 and not self.boom:
            self.index = 0
        if self.boom:
            if self.index < 2.5:
                self.index = 2.5
            if self.index >= 4:
                self.index = 0
                self.boom = False
                self.kill()
        self.image = self.images[math.floor(self.index)]

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)


class UFO(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize and set its starting position."""
        super(UFO, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings


        # Load the ship image, and get its rect.
        self.image = pygame.image.load('/Users/gregoryvasquez/PycharmProjects/spaceInvaders/images/enemy_ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # Start each new ship at the bottom center of the screen.
        self.rect.left = self.screen_rect.left
        self.rect.top = self.screen_rect.top + 100

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags.
        self.moving_right = True
        self.moving_left = False

        self.boom = False

    def update(self, screen):
        if self.moving_right:
            self.rect.centerx += 2
            if self.rect.centerx > self.screen_rect.right:
                self.rect.left -= 4000
        if self.boom is True:
            self.rect.left -= 2000

            self.boom = False


    def blitme(self):
        self.screen.blit(self.image, self.rect)
