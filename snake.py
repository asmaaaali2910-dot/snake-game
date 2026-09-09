from turtle import Turtle 


class Snake ():
    def __init__(self):
        self.turtles=[]
        self.position=[(-20,0),(0,0),(20,0)]
        self.creat_body() 
        self.head = self.turtles[-1]
        
    def creat_body(self):
        for i in range (len(self.position)):
            turtle=Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.shapesize(1,1)
            turtle.goto(self.position[i])
            self.turtles.append(turtle)
            
    def extend (self):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.turtles[0].pos())
        self.turtles.insert(0,new_segment)
  
            
            
    def move (self):
        for i in range (len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.forward(20)
        
        
    def up(self):
        self.head.setheading(90)
    def down (self):
        self.head.setheading(270)
    def right(self):
        self.head.setheading(0)
    def left(self):
        self.head.setheading(180)
        