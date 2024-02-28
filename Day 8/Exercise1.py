import math

_height = int(input("Height of the wall: "))
_width = int(input("Width of the wall: "))
coverage = 5

def paint_calc(height, width, cover):
  cans = math.ceil((height * width) / cover)
  print(f"Total number of cans need are {cans}")
  
paint_calc(height = _height, width = _width, cover = coverage)