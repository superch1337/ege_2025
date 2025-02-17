import turtle as t
t.tracer(0)
t.left(90)
t.width(5)
a = 55

for i in range(5):
    t.fd(7*a)
    t.rt(90)
    t.fd(4*a)
    t.rt(90)

t.up()
for x in range(20,-20,-1):
    for y in range(20,-20,-1):
        t.goto(x*a,y*a)
        t.dot(4,'red')
t.down()
t.done()

