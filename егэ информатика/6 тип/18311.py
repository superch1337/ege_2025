import turtle as t
t.tracer(0)
t.lt(90)
t.width(5)
a = 10

for i in range(5):
    t.fd(15*a)
    t.lt(90)
    t.fd(25*a)
    t.lt(90)

t.up()

t.fd(4*a)
t.lt(90)
t.fd(12*a)
t.lt(90)

t.down()
for i in range(6):
    t.fd(38*a)
    t.lt(90)
    t.fd(22*a)
    t.lt(90)

t.up()
for x in range(100,-100,-1):
    for y in range(100,-100,-1):
        t.goto(x*a,y*a)
        t.dot(4,'red')
t.down()
t.done()