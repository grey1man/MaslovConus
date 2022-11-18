from Drawer import Drawer
from Primitives import Cone
import pygame
import sys
from threading import Thread

cone = Cone(1, 0.5)
drawer = Drawer()
drawer.setObjectToDraw(cone)
drawer.start()