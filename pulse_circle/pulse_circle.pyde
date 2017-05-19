class PulseCircle:
    on = False
    spinning = False
    pulseAngle = 0

    def __init__(self, xpos, ypos, radius):
        self.x = xpos
        self.y = ypos
        self.r = radius
        self.ri = radius
        self.on = True

    def pulse(self, speed, rmax):
        if self.on == True:
            self.r = self.ri + rmax * sin(radians(self.pulseAngle))
            self.pulseAngle += speed

    def display(self):
        if self.on == True:
            pushMatrix()
            translate(self.x, self.y)
            ellipse(0, 0, self.r, self.r)
            popMatrix()
