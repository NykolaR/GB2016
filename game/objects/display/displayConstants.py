# Display constants

size = width, height = 160, 144
fps = 60


c1 = 0xE4, 0xFD, 0xE1 # Light green
c2 = 0x8A, 0xCB, 0x88 # Dull green
c3 = 0xA7, 0x26, 0x08 # Dark orange
c4 = 0x09, 0x0C, 0x02 # Dark grey
c5 = 0, 0, 0, 0 # Transparent

# full pallete
# background tiles use 4 colors, sprites, 3 + transparent
palette = [ c1, c2, c3, c4 ]

# sprite palletes
# [0] is a 'light' shade
# [1] is a 'shading' shade
# [2] is a 'dark' shade
# [3] is transparent
paletteS1 = [ c2, c3, c4, c5]
paletteS2 = [ c1, c2, c4, c5]
