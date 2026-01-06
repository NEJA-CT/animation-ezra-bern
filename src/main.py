import pyxel
import math
import random

from lib.util import *

GRAVITY = 2
BOUNCE = 1
W, H = 160, 120
x, y = W // 2, H // 2
vx, vy = 0, 0

def update():
   global  y,vy,x,vx


   vx += GRAVITY
   x += vx
   vy += GRAVITY
   y += vy

   #if pyxel.btnp(pyxel.KEY_RIGHT):
      #vx += GRAVITY
      #x += vx

   if pyxel.btnp(pyxel.KEY_DOWN):
      vy -= vy + GRAVITY * 0.1
   if pyxel.btnp(pyxel.KEY_UP):
      vy += vy + GRAVITY * 0.1
   if pyxel.btnp(pyxel.KEY_LEFT):
      vx += vx + BOUNCE * 0.1
   if pyxel.btnp(pyxel.KEY_RIGHT):
      vx -= vx + BOUNCE * 0.1
   

   ceiling = 33
   if y < ceiling:
      y = ceiling
      vy = -vy * BOUNCE
   wall = W - 33
   if x > wall:
      x = wall
      vx = -vx * BOUNCE

   leftwall = 33
   if x < leftwall:
      x = leftwall
      vx = -vx * BOUNCE
   
   ground = H - 33
   if y > ground:
       y = ground
       vy = -vy * BOUNCE

   

def draw():
   pyxel.cls(0)

   pyxel.circb(x,y,30,7)
   pyxel.circ(x, y, 7, 0)
   pyxel.circ(x+30,y,3,7)
   pyxel.circ(x,y+30,3,7)
   pyxel.circ(x,y-30,3,7)
   pyxel.circ(x-30,y,3,7)
   pyxel.circ(x-15,y+15,3,7)
   pyxel.circ(x+15,y-15,3,7)
   pyxel.circ(x+15,y+15,3,7)
   pyxel.circ(x-15,y-15,3,7)
pyxel.init(W,H,title="ezras pyxel thing")
pyxel.run(update,draw)