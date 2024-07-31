import turtle

def pattern_generator(sides, size, repetitions, angle):
    for _ in range(repetitions):
        for _ in range(sides):
            turtle.forward(sides)
            turtle.left(360 / sides)
        turtle.left(angle)
turtle.speed(0) # Prędkość
turtle.pencolor("green")
pattern_generator(sides=19, size=100, repetitions=36, angle=10)
turtle.done() 