# Kiwi, 2021.08.28
# Quadtree collisions with Daniel Shiffman of the Coding Train
# Coding Challenge #98.3: Quadtree Collisions - Part 3
# https://www.youtube.com/watch?v=z0YFFg_nBjw
# translation to Python
#
# TODO: different particle sizes. collision detect that
# TODO: implement a circle class instead of Rect that our quadtree uses as a range


from Particle import *
from Quadtree import *
from Point import *
from Rectangle import *

        
def setup():
    global particles
    
    frameRate(144)
    colorMode(HSB, 360, 100, 100, 100)

    
    size(600, 400)
    particles = []
    
    # populate particles
    for i in range(1000):
        
        x = randomGaussian() * (width * 0.2) + width/2
        y = randomGaussian() * (height * 0.2) + height/2
        
        x = constrain(x, 0, width)
        y = constrain(y, 0, height)
        
        p = Particle(x, y)
        particles.append(p)
        
    
def draw():
    global particles
    
    background(209, 95, 33)
    
    # recreate the quad tree every frame
        
    boundary = Rectangle(0, 0, width, height)
    qt = Quadtree(boundary, 4)
    
    for particle in particles:
        p = Point(particle.x, particle.y, particle)
        qt.insert(p)
        
    
    R = 12 # radius of bounding box
    # check if particles collide
    for particle in particles:
        points = qt.query(Rectangle(particle.x-R, particle.y-R, 2*R, 2*R))
        for p in points:
            other = p.data
            if particle != other and particle.intersects(other):
                particle.highlight()
                # other.data.highlight()
    
    qt.show()            
    
    for p in particles:
        p.move()
        p.render()
    
    
    
    fill(0, 0, 100)
    textSize(15)
    text("{}".format(frameRate), 20, 30)
