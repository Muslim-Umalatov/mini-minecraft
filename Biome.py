from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image  # For loading the texture image
import numpy as np
from Blocks import *
import pygame
import random

forest_positions = []  # Ağaçların sabit konumlarını saklamak için liste
cactus_positions = []  # Kaktüslerin sabit konumlarını saklamak için liste


def init_biome_positions():
    global forest_positions
    global cactus_positions
    forest_positions = [(random.randint(0, 45), random.randint(-45, 45)) for i in range(1)]
    cactus_positions = [(random.randint(-45, -5), random.randint(-45, 45)) for i in range(20)]


def draw_sand_ground():
    glBindTexture(GL_TEXTURE_2D, 6)
    glBegin(GL_QUADS)
    for x in range(-50, 0, 10):
        for z in range(-50, 51, 10):
            # Küplerin yüksekliğini rastgele belirleyelim
            y1 = 0  # Set a fixed height for the ground
            y2 = 0  # Set a fixed height for the ground
            glTexCoord2f(0.0, 0.0)
            glVertex3f(x, y1, z)
            glTexCoord2f(1.0, 0.0)
            glVertex3f(x + 10, y2, z)
            glTexCoord2f(1.0, 1.0)
            glVertex3f(x + 10, y2, z + 10)
            glTexCoord2f(0.0, 1.0)
            glVertex3f(x, y1, z + 10)
    glEnd()
    glBindTexture(GL_TEXTURE_2D, 0)  # Texture binding'i sıfırla


def draw_ground():
    glBindTexture(GL_TEXTURE_2D, 7)
    glBegin(GL_QUADS)
    for x in range(0, 50, 10):
        for z in range(-50, 51, 10):
            # Küplerin yüksekliğini rastgele belirleyelim
            y1 = 0  # Set a fixed height for the ground
            y2 = 0  # Set a fixed height for the ground
            glTexCoord2f(0.0, 0.0)
            glVertex3f(x, y1, z)
            glTexCoord2f(1.0, 0.0)
            glVertex3f(x + 10, y2, z)
            glTexCoord2f(1.0, 1.0)
            glVertex3f(x + 10, y2, z + 10)
            glTexCoord2f(0.0, 1.0)
            glVertex3f(x, y1, z + 10)
    glEnd()
    glBindTexture(GL_TEXTURE_2D, 0)  # Texture binding'i sıfırla


def draw_tree(x, z):
    # Wood positions
    wood_positions = [
        (x, 0, z),
        (x, 1, z),
        (x, 2, z),
        (x, 3, z),
        (x, 4, z)
    ]
    for pos in wood_positions:
        glPushMatrix()
        glTranslatef(*pos)
        cube(4)  # all coordinates defined in Blocks file
        glPopMatrix()

    # Draw leaves as blocks
    leaf_positions = [
        # Top
        (x+1, 2, z+2), (x, 2, z+2), (x-1, 2, z+2),
        (x+2, 2, z+1), (x+1, 2, z+1), (x, 2, z+1), (x-1, 2, z+1), (x-2, 2, z+1),
        (x+2, 2, z), (x+1, 2, z), (x-1, 2, z), (x-2, 2, z),
        (x+2, 2, z-1), (x+1, 2, z-1), (x, 2, z-1), (x-1, 2, z-1), (x-2, 2, z-1),
        (x+1, 2, z-2), (x, 2, z-2), (x-1, 2, z-2),
        # Bottom

        # Top
        (x+1, 3, z+2), (x, 3, z+2), (x-1, 3, z+2),
        (x+2, 3, z+1), (x+1, 3, z+1), (x, 3, z+1), (x-1, 3, z+1), (x-2, 3, z+1),
        (x+2, 3, z), (x+1, 3, z), (x-1, 3, z), (x-2, 3, z),
        (x+2, 3, z-1), (x+1, 3, z-1), (x, 3, z-1), (x-1, 3, z-1), (x-2, 3, z-1),
        (x+1, 3, z-2), (x, 3, z-2), (x-1, 3, z-2),
        # Bottom

        # Top
        (x, 4, z+1),
        (x+1, 4, z), (x-1, 4, z),
        (x, 4, z-1),
        # Bottom

        # Top
        (x, 5, z+1),
        (x+1, 5, z), (x, 5, z), (x-1, 5, z),
        (x, 5, z-1),
        # Bottom
    ]

    for pos in leaf_positions:
         glPushMatrix()
         glTranslatef(*pos)
         cube(1)  # all coordinates defined in Blocks file
         glPopMatrix()


def draw_cactus(x, z):
    # Cactus positions
    cactus_positions = [
        (x, 0, z),
        (x, 1, z),
        (x, 2, z)
    ]
    for pos in cactus_positions:
        glPushMatrix()
        glTranslatef(*pos)
        cube(3)
        glPopMatrix()


def draw_forest():
    global forest_positions
    global cactus_positions
    for x, z in forest_positions:
        draw_tree(x, z)
    for x, z in cactus_positions:
        draw_cactus(x, z)


