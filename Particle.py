class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 2
        self.highlighted = False
    
    
    def move(self):
        JITTER = 5
        self.x += random(-JITTER, JITTER)
        self.y += random(-JITTER, JITTER)
    
    
    def render(self):
        noStroke()
        
        fill(0, 0, 70)        
        if self.highlighted:
            fill(0, 0, 100)
        
        circle(self.x, self.y, self.r*2)
        self.highlighted = False
       
       
    def highlight(self):
        self.highlighted = True
       
           
    def intersects(self, other):
        # check if distance is less than sum of the radii
        distance = dist(self.x, self.y, other.x, other.y)
        if distance < self.r + other.r:
            return True
        else:
            return False   
