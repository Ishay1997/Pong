from turtle import Turtle

UP = 90
DOWN = 270



class Paddle(Turtle):
    def __init__(self, Positions):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(Positions)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    # def create_paddle(self):
    #
    #     # self.segments.append(new_segment)
    #
    # def move(self):
    #     for seg_num in range(len(self.segments)-1, 0, -1):
    #         new_y = self.segments[seg_num - 1].ycor()
    #         self.segments[seg_num].goto(self.segments[0].xcor(), new_y)
    #
    # def up(self):
    #     self.head.setheading(UP)
    #
    # def down(self):
    #     self.head.setheading(DOWN)