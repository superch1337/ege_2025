import turtle as t

t.tracer(0)
t.left(90)
t.width(8)
a = 25

for i in range(4):
    t.fd(6*a)
    t.rt(90)
    t.fd(6*a)
    t.lt(90)
    t.fd(6*a)
    t.rt(90)
t.up()
for x in range(25,-25,-1):
    for y in range(25,-25,-1):
        t.goto(x*a,y*a)
        t.dot(4,'red')
t.down()
t.done()
