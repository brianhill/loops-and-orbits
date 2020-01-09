# https://www.youtube.com/watch?v=1wl5nu6QGC0

from vpython import *
ground=box(pos=vector(0,0,0), size=vector(10,0.2,1), color=color.green)
ball=sphere(pos=vector(-4.5,0,0), radius=0.2, color=color.yellow)

g=vector(0,-9.8,0)
v0=8
theta=30*pi/180
# v0x = v0 * cos(theta)
# v0y = v0 * sin(theta)

ball.m=0.5

ball.v=vector(0,v0,0)


t=0
dt=0.01

attach_trail(ball)

while ball.pos.y>=0:
  rate(100)
  F=ball.m*g
  ball.v=ball.v+(F/ball.m)*dt
  ball.pos=ball.pos+ball.v*dt/ball.m
  t=t+dt

print(t)
