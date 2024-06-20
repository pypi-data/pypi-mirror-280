# SPDX-FileCopyrightText: 2023 Justus Perlwitz
# SPDX-FileCopyrightText: 2024 Justus Perlwitz
#
# SPDX-License-Identifier: MIT

from pathlib import Path
from time import sleep


from pomoglorbo.core.util import in_app_resource
from pomoglorbo.types import PathOrResource
import os



def play(path: PathOrResource, volume: float, block: bool = True) -> None:
    os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = ""
    import pygame
    pygame.mixer.init()
    match path:
        case Path():
            sound = pygame.mixer.Sound(path)
        case str():
            sound = pygame.mixer.Sound(buffer=in_app_resource(path))
    sound.set_volume(volume)
    sound.play()
    if not block:
        return
    while pygame.mixer.get_busy():
        sleep(0.1)
