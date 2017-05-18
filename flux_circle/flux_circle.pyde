class FluxCircle:
    steps = 200

    def __init__(self, xpos, ypos, radius, smoothness):
        self.x = xpos
        self.y = ypos
        self.r = radius
        self.s = smoothness

    def grow(self, radius, speed):
        if self.r < radius:
            self.r += speed

    def display(self):
        r = self.r
        s = self.s
        pushMatrix()
        translate(self.x, self.y)
        beginShape()
        for i in range(self.steps):
            angle = i * TWO_PI / self.steps
            x = cos(angle)
            y = sin(angle)
            curveVertex(x * random(r - s, r + s), y * random(r - s, r + s))
        endShape(CLOSE)
        popMatrix()
