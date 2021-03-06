from PIL import Image, ImageOps
import numpy as np
import queue
class Point(object):
      def __init__(self, x, y):
            self.x = x
            self.y = y   
      def add(self, point):
            self.x += point.x
            self.y += point.y 

class Dots(object):      
      def __init__(self):
            self.point = Point(0, 0)
            self.num = 0
      def addDot(self, point):
            self.point.add(point)
            self.num += 1
      
      def getCenter(self):
          return Point(self.point.x / self.num, self.point.y / self.num)

move = [-1, 0, 1] 
def around(dots, matrix , point):
      queue1 = queue.Queue()
      queue1.put(point)
      shape = matrix.shape
      while not queue1.empty() :
            point1 = queue1.get()
            if matrix[point1.x][point1.y] == 0:
                  continue
            matrix[point1.x][point1.y] = 0         
            dots.addDot(point1)
            for i in move:
                  for j in move:
                        newX = point1.x + i
                        newY = point1.y + j 
                        if (newX < 0 or newX >= shape[0] or newY < 0 or newY >= shape[1]):
                              continue
                        newPoint = Point(newX, newY)
                        queue1.put(newPoint)


name = input("Enter full name of the image (default:data.png): ")
if len(name) == 0:
      name = "data.png"
image = Image.open(name, 'r')
thresh = 200
fn = lambda x : 255 if x > thresh else 0
r = image.convert('L').point(fn, mode='1')

list = []
matrix = np.array(r)

shape = matrix.shape
for x in range(shape[0]):
      for y in range(shape[1]):
            if (matrix[x][y] == 0):
                  continue
            dots = Dots()
            point = Point(x, y)
            around(dots, matrix, point)
            list.append(dots.getCenter())

f = open("fuck.txt", "w+")
                  
centers = np.zeros((shape[0] * 10, shape[1] * 10))
newMatrix = np.array(r)
for point in list:
      f.write("Center=(%d, %d)\n" % (point.x, point.y))
      x = round(point.x)
      y = round(point.y)
      newMatrix[x][y] = not newMatrix[x][y] 
print("Calculation done.")
Image.fromarray(newMatrix).show()      
f.close()

