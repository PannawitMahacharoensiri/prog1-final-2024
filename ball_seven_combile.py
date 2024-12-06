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

    def move_ball(self,dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def update_ball_velocity(self):
        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.x) > (self.canvas_width - self.ball_radius):
            self.vx = -self.vx

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.y) > (self.canvas_height - self.ball_radius):
            self.vy = -self.vy


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
                i.move_ball(dt)
                i.update_ball_velocity()
            turtle.update()

"""
            drawer = turtle.Turtle()
            seven = Seven(drawer, "red")
            seven.run()
"""


    # turtle.done()
class Seven:
    def __init__(self,my_turtle,color):
        self.my_turtle = my_turtle
        self.color = color
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.my_turtle.color(color)
        self.my_turtle.penup()
        self.my_turtle.setheading(0)
        self.my_turtle.goto(0, 0)
        self.my_turtle.pensize(10)

    def draw(self, digit):
        if digit == 0:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.penup()

        if digit == 1:
            self.my_turtle.goto(50, 100)
            self.my_turtle.pendown()
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.penup()

        if digit == 2:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.penup()

        if digit == 3:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(-100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.left(90)
            self.my_turtle.penup()

        if digit == 4:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.forward(-100)
            self.my_turtle.forward(-100)
            self.my_turtle.right(90)
            self.my_turtle.penup()

        if digit == 5:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.forward(-100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.left(90)
            self.my_turtle.penup()

        if digit == 6:
            self.draw( 5)
            self.my_turtle.goto(-50, 0)
            self.my_turtle.pendown()
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.penup()

        if digit == 7:
            self.my_turtle.goto(-50, 100)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.forward(-100)
            self.draw(1)

        if digit == 8:
            self.draw( 0)
            self.my_turtle.goto(-50, 0)
            self.my_turtle.pendown()
            self.my_turtle.forward(100)
            self.my_turtle.penup()

        if digit == 9:
            self.draw( 5)
            self.my_turtle.goto(50, 100)
            self.my_turtle.pendown()
            self.my_turtle.right(90)
            self.my_turtle.forward(100)
            self.my_turtle.left(90)
            self.my_turtle.penup()

    def clear(self):
        self.my_turtle.clear()

    @staticmethod
    def my_delay(dt):
        import time
        start = time.time()
        while time.time() - start < dt:
            pass

    def run(self):
        delay_in_seconds = 0.2
        while True:
            for i in range(0, 10):
                self.clear()
                self.draw( i)
                self.my_delay(delay_in_seconds)
                turtle.update()

Test = Run_ball(7)
Test.run()

# turtle.colormode(255)




