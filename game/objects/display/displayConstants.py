# Display constants
import pygame

pygame.init ()

size = width, height = 160, 144 # 20x18
fps = 60

c5 = 0, 0, 0 # "transparent" (shouldn't be used)

palettes = {
            0 : [
                [0xE1, 0xF9, 0xA9], # Light green
                [0x76, 0xA8, 0x03], # Mid Green
                [0x3E, 0x51, 0x12], # Dark Green
                [0x18, 0x1C, 0x0F] # "Black"
                ],
            1 : [
                [0xD9, 0xF4, 0xF4], # Light blue
                [0x54, 0xFF, 0xFF], # Mid
                [0x79, 0x9E, 0x9E], # Dark
                [0x4E, 0x66, 0x66] # "Black"
                ],
            2 : [
                [0xF7, 0xDB, 0xFF], #Purple
                [0xE5, 0x7F, 0xFF],
                [0xCB, 0x62, 0xE5],
                [0x30, 0x01, 0x1E]
                ],
            3 : [
                [0xE5, 0xC2, 0xC0], # Red
                [0xD6, 0x93, 0x8F],
                [0x9E, 0x36, 0x31],
                [0x5B, 0x10, 0x0C]
                ],
            4 : [
                [0xF2, 0xEF, 0xEA], #Brown
                [0xDB, 0xB3, 0x6D],
                [0xFC, 0xBE, 0x53],
                [0x59, 0x4F, 0x3D]
                ],
            # non-monochrome:
            5 : [
                [0xE4, 0xFD, 0xE1], # Light green
                [0x8A, 0xCB, 0x88], # Dull green
                [0xA7, 0x26, 0x08], # Dark orange
                [0x09, 0x0C, 0x02] # Dark grey
                ],
            6 : [
                [0xF7, 0xEC, 0xE1], # White
                [0x90, 0x67, 0xC6], # Purple shade
                [0xDB, 0x2B, 0x39], # Red highlight
                [0x24, 0x20, 0x38] # Dark grey
                ],
            7 : [
                [0xFF, 0xFF, 0xFF], # Snow
                [0xD7, 0x26, 0x38], # Salmon
                [0xFF, 0x57, 0x0A], # Sun
                [0x42, 0x00, 0x39] # Sinister purple
                ],
            8 : [
                [0xF3, 0xFC, 0xF0], # White
                [0xFF, 0xD2, 0x3F], # Peach
                [0x54, 0x0D, 0x6E], # Purple
                [0x1F, 0x27, 0x1B] # Black
                ]
        }


# full pallete
# background tiles use 4 colors, sprites, 3 + transparent
palette = palettes [0]
paletteS1 = [ palette [0], palette [1], palette [2], c5]
paletteS2 = [ palette [1], palette [2], palette [3], c5]

def setPalette (pal):
    palette = palettes [pal]
    paletteS1 [0] = palette [0]
    paletteS1 [1] = palette [1]
    paletteS1 [2] = palette [2]
    paletteS1 [3] = palette [3]
    paletteS2 = [ palette [1], palette [2], palette [3], c5]

# sprite palletes
# [0] is a 'light' shade
# [1] is a 'shading' shade
# [2] is a 'dark' shade
# [3] is transparent, and shouldn't be called
