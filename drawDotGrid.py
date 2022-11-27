# This script draws a number of square shapped grid patterns (as used in The Nature Game)
# You might want to customize the vertToHorzRatio depending on your paper format, or how many figures to print depending on how much paper you want to use
import sys
from PIL import Image, ImageDraw
import PIL
A4VertToHorzRatio = 842/595

horzSize = 1000
vertSize = int(horzSize*A4VertToHorzRatio)
im = Image.new('P', (horzSize,vertSize), 'white')

draw = ImageDraw.Draw(im)
nbHorzDotsPerFigure = 5
nbVertDotsPerFigure = 5
nbHorzFigures=6
nbVertFigures=int(nbHorzFigures*A4VertToHorzRatio)

nbHorzDots = nbHorzDotsPerFigure*nbHorzFigures
nbVertDots = nbVertDotsPerFigure*nbVertFigures

horzSpacingDots = nbHorzDots+nbHorzFigures
vertSpacingDots = nbVertDots+nbVertFigures

horzSpacing = horzSize/horzSpacingDots
vertSpacing = vertSize/vertSpacingDots

# Draw a cross at every correct intersection to draw the grids
for i in range(horzSpacingDots): 
    for j in range(vertSpacingDots):
        # skip drawing a cross in between the grids
        if (i%(nbHorzDotsPerFigure+1) == 0): 
            continue
        if (j%(nbVertDotsPerFigure+1) == 0): 
            continue
        # horizontal line
        draw.line((i*horzSpacing-1,j*vertSpacing , i*horzSpacing+1, j*vertSpacing), 'black')
        # vert line
        draw.line((i*horzSpacing,j*vertSpacing-1 , i*horzSpacing, j*vertSpacing+1), 'black')


# write to stdout
im.save('./grid.png', "PNG")
