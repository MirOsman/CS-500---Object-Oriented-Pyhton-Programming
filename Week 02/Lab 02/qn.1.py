import math

circle1 = input("Enter circle1's center x-, y-coordinates, and radius: ").split(" ")
circle2 = input("Enter circle2's center x-, y-coordinates, and radius: ").split(" ")


def check(circle1, circle2):
  # convert data inside lists before from strings to floats to do maths
  circle1 = [float(i) for i in circle1]
  circle2 = [float(i) for i in circle2]

  x1,y1 = circle1[0],circle1[1]
  x2,y2 = circle2[0],circle2[1]
  r1, r2 = circle1[2], circle2[2]
  distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
  
  if distance <= abs(r1-r2):
    if r1>r2:
      print("circle2 is inside circle1")
    else:
      print("circle1 is inside circle2")
  else:
    print("circle2 overlaps circle1")
    

check(circle1, circle2)
