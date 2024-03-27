from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_body(position)

    def add_body(self,position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.all_snakes.append(tim)

    def extend(self):
        self.add_body(self.all_snakes[-1].position())

    def move(self):
        for num in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[num - 1].xcor()
            new_y = self.all_snakes[num - 1].ycor()
            self.all_snakes[num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)