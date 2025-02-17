from turtle import *
tracer(0)
lt(90)
width(3)
a = 10

rt(45)
for i in range(7):
    fd(5*a)
    rt(45)
    fd(10*a)
    rt(135)

up()
for x in range(20,-20,-1):
    for y in range(20,-20,-1):
        goto(x*a,y*a)
        dot(4,'red')

down()
done()