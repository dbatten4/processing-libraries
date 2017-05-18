class BeadRing:
    on = False
    angle = 0
    spinning = False

    def __init__(self, xpos, ypos, radius, num, beadRadius):
        self.x = xpos
        self.y = ypos
        self.r = radius
        self.n = num
        self.br = beadRadius
        self.on = True

    def grow(self, speed, rmax):
        if self.on == True:
            self.r += speed
            if self.r >= rmax:
                self.on = False

    def spin(self, speed, orientation):
        self.spinning = True
        self.spinSpeed = speed
        self.orientation = orientation

    def display(self):
        if self.on == True:
            pushMatrix()
            translate(self.x, self.y)
            if self.spinning == True:
                rotate(self.angle)
            for i in range(self.n):
                angle = TWO_PI / self.n
                ellipse(0, -self.r, self.br, self.br)
                rotate(angle)
            self.angle += self.orientation * self.spinSpeed
            popMatrix()
