import turtle
import random

class Ball:
    def __init__(self,x,y,vx,vy,ball_color,id):
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ball_color = ball_color
        self.id = id

    def draw_ball(self):
        turtle.hideturtle()
        turtle.speed(0)
        turtle.tracer(0)
        turtle.colormode(255)
        turtle.penup()
        turtle.color(self.ball_color)
        turtle.fillcolor(self.ball_color)
        turtle.goto(self.x, self.y - self.ball_radius)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.ball_radius)
        turtle.end_fill()

    def move_ball(self, i):
        self.x[i] += self.vx[i] * dt
        self.y[i] += self.vy[i] * dt

    def update_ball_velocity(self, i):
        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.x[i]) > (self.canvas_width - self.ball_radius):
            self.vx[i] = -self.vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.y[i]) > (self.canvas_height - self.ball_radius):
            self.vy[i] = -self.vy[i]


class Run_ball:
    def __init__(self, num_balls = 5):
        self.num_balls = num_balls
        self.ball_lists = []
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]

        for i in range(self.num_balls):
            x = -self.canvas_width + (i+1)*(2*self.canvas_width/(self.num_balls+1))
            y = 0.0
            vx = 10*random.uniform(-1.0, 1.0)
            vy = 10*random.uniform(-1.0, 1.0)
            ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.ball_lists.append(Ball(x, y, vx, vy, ball_color, i))

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)

    def run(self):
        dt = 0.2  # time step
        while (True):
            turtle.clear()
            self.draw_border()
            for i in self.ball_lists:
                i.draw_ball()
                # i.move_ball(i)
                # i.ball.update_ball_velocity()
            turtle.update()



    # turtle.done()


Test = Run_ball(7)
Test.run()
# turtle.colormode(255)




