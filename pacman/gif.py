# Copyright (C) 2021 @ctrysbita @x-mug
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from typing import List

import pygame
from PIL import Image, ImageSequence


class Gif:
    """Load GIF format image to pygame."""
    def __init__(self, path: str, size=None):
        self.index = 0
        self.frames: List[pygame.surface.Surface] = []

        image: Image.Image = Image.open(path)
        assert image.format == 'GIF'

        for frame in ImageSequence.Iterator(image):
            frame: Image.Image = frame.convert('RGBA')
            if size:
                frame = frame.resize(size)
            surface = pygame.image.frombuffer(frame.tobytes(), frame.size,
                                              frame.mode).convert_alpha()
            self.frames.append(surface)

        self.length = len(self.frames)

    def get_frame(self):
        """Get next frame."""
        self.index = self.index + 1 if self.index < self.length - 1 else 0
        return self.frames[self.index]
