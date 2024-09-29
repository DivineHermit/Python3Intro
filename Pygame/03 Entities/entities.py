"""
    This file will hold the characters, NPCs and player character.
"""
import pygame

import settings
from main import Game


class Entity(pygame.sprite.Sprite):
    """ The base blueprint for game characters. """
    def __init__(self) -> None:
        self._layer = settings.LAYER_CHARACTERS
        self.groups = Game.sg_all_sprites
        super().__init__(self, self.groups)
        # Sprite appearance.
        self.image = pygame.Surface((20, 50))
        self.image.fill((200, 200, 0))
        self.rect = self.image.get_rect()
        self.rect.center = settings.WINDOW_CENTER
