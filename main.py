import pgzrun, random

balls=[]
colours=["red","orange","yellow","green","blue","purple","pink"]

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

for x in range(random.randint(2,10)):
    ball=Ball(random.randint(50,450),250,random.choice(colours),random.randint(5,50))
    balls.append(ball)


def update(dt):
    #building formula which will accelerate constantly
    for ball in balls:
        yvelocity=ball.yvelocity
        gravity=random.randint(0,5000)
        ball.yvelocity+=gravity*dt
        ball.y+=(yvelocity+ball.yvelocity)*0.5*dt
        if ball.y > HEIGHT-ball.radius:
            ball.y=HEIGHT-ball.radius
            ball.yvelocity=-ball.yvelocity*0.9

def draw():
    screen.clear()
    for ball in balls:
        ball.drawball()

pgzrun.go()