import pymunk

space = pymunk.Space()
space.gravity = 0,-1000
print(space)
body = pymunk.Body(1,1666)
body.position = 50,100

poly = pymunk.Poly.create_box(body)
space.add(body, poly)

while True:
    space.step(0.02)
