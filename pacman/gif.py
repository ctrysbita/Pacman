from typing import List

import pygame
from PIL import Image, ImageSequence


class Gif:
    def __init__(self, path: str, size=None):
        self.index = 0
        self.frames: List[pygame.surface.Surface] = []

        image: Image.Image = Image.open(path)
        assert image.format == 'GIF'

        for frame in ImageSequence.Iterator(image):
            frame: Image.Image = frame.convert('RGBA')
            if size:
                frame = frame.resize(size)
            surface = pygame.image.frombuffer(frame.tobytes(),
                                              frame.size,
                                              frame.mode).convert_alpha()
            self.frames.append(surface)

        self.length = len(self.frames)

    def get_frame(self):
        self.index = self.index + 1 if self.index < self.length - 1 else 0
        return self.frames[self.index]
