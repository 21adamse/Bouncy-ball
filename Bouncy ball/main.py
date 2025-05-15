import pgzrun

HEIGHT = 500
WIDTH = 700

class Ball():
    def __init__(self,x,y,colour,radius):
        self.x = x
        self.y = y
        self.colour = colour
        self.radius = radius
        self.xvelocity = 10
        self.yvelocity = 0
    def drawball(self):
        screen.draw.filled_circle((self.x,self.y),self.radius,self.colour)

ball=Ball(350,250,"red",25)
gravity=2000

def update(dt):
    #building formula which will accelerate constantly
    yvelocity=ball.yvelocity
    ball.yvelocity+=gravity*dt
    ball.y+=(yvelocity+ball.yvelocity)*0.5*dt
    if ball.y > HEIGHT-ball.radius:
        ball.y=HEIGHT-ball.radius
        ball.yvelocity=-ball.yvelocity*0.9

def draw():
    screen.clear()
    ball.drawball()

pgzrun.go()