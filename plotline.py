from math import sin, cos
import time
import random

def sign(x):
   if x > 0:
      return 1
   return -1

def plot(x,y, flipAboutX, y0, flipAboutY, x0, swapXY):
   if flipAboutY:
      x = 2*x0 - x
   if flipAboutX:
      y = 2*y0 - y
   if swapXY:
      x,y = y,x
   try:
      A[y][x] = 1
   except:
      pass

   
def plotLine(A, x0,y0, x1,y1):
   dx=x1-x0
   dy=y1-y0

   flipAboutX = 0
   flipAboutY = 0
   swapXY = 0

   if abs(dy) > abs(dx):
      swapXY = 1
      dy, dx = dx, dy
      x1, y1 = y1, x1
      x0, y0 = y0, x0

   if dy < 0:
      flipAboutX = 1
      y1 = 2*y0 - y1
      dy = -dy

   if dx < 0:
      flipAboutY = 1
      x1 = 2*x0 - x1
      dx = -dx


   D = 2*dy - dx
   plot(x0, y0, flipAboutX, y0, flipAboutY, x0, swapXY)
   y=y0

   for x in range(x0+1, x1+1):
      if D > 0:
         y = y+1
         plot(x, y, flipAboutX, y0, flipAboutY, x0, swapXY)
         D = D + (2*dy-2*dx)
      else:
         plot(x, y, flipAboutX, y0, flipAboutY, x0, swapXY)
         D = D + (2*dy)

width = 35
height = 30

A = [[0 for i in range(width)] for i in range(height)]

#ax, bx, cx = [random.randint(0,width-1) for i in range(3)]
#ay, by, cy = [random.randint(0,height-1) for i in range(3)]

ax,bx,cx = 10, 12, 13
ay,by,cy = 2,20,2


plotLine(A, ax, ay, bx, by)
plotLine(A, ax, ay, cx, cy)
plotLine(A, bx, by, cx, cy)

def fillTri(A, ax, ay, bx, by, cx, cy):
   for y in range(len(A)):
      ranges = []

      n = 0
      lastWasFilled = False
      a = -1
      b = -1

      for i, c in enumerate(A[y]):
         if c == 1:
            if not lastWasFilled:
               a = i
               b = i
               lastWasFilled = True
            else:
               b = i
         else:
            if lastWasFilled:
               ranges.append([a,b])
               a = b = -1
               lastWasFilled = False
      if lastWasFilled:
         ranges.append([a,b])
         a = b = -1
         lastWasFilled = False

      print ranges
               

def zCompOfCrossProd(ax, ay, bx, by):
   return ax*by - ay*bx

def isPointInsideTriangle(px, py, ax, ay, bx, by, cx, cy):
   r_pa_x = px - ax
   r_pa_y = py - ay

   r_pb_x = px - bx
   r_pb_y = py - by

   r_pc_x = px - cx
   r_pc_y = py - cy

   r_ba_x = bx - ax
   r_cb_x = cx - bx
   r_ac_x = ax - cx

   r_ba_y = by - ay
   r_cb_y = cy - by
   r_ac_y = ay - cy

   u = zCompOfCrossProd(r_ba_x, r_ba_y, r_pa_x, r_pa_y)
   v = zCompOfCrossProd(r_cb_x, r_cb_y, r_pb_x, r_pb_y)
   w = zCompOfCrossProd(r_ac_x, r_ac_y, r_pc_x, r_pc_y)

   if u >= 0 and v >= 0 and w >= 0:
      return 1
   if u <= 0 and v <= 0 and w <= 0:
      return 1

   return 0


fillTri(A, ax, ay, bx, by, cx, cy)

for y in (A):
   print " ".join(["x" if _ else " " for _ in y])
