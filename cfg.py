'''Config File'''
import os


'''Define some colors to use'''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
SKYBLUE = (0, 191, 255)

'''All game resources path'''
Base_path = os.path.abspath(os.path.split(os.path.abspath(os.path.realpath(__file__)))[0])
BGMPATH = os.path.join(Base_path, 'resources/sounds/bg.mp3')
ICONPATH = os.path.join(Base_path, 'resources/images/icon.png')
FONTPATH = os.path.join(Base_path, 'resources/font/ALGER.TTF')
HEROPATH = os.path.join(Base_path, 'resources/images/pacman.png')
BlinkyPATH = os.path.join(Base_path, 'resources/images/Blinky.png')
ClydePATH = os.path.join(Base_path, 'resources/images/Clyde.png')
InkyPATH = os.path.join(Base_path, 'resources/images/Inky.png')
PinkyPATH = os.path.join(Base_path, 'resources/images/Pinky.png')