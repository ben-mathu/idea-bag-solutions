import sys
import math
  
def main(point_1, point_2) -> int:
  '''
    This command line application receives co-ordinates in this
    form: python <distance...>.py <point_1_x> <point_1_y> <point_2_x> <point_2_y>
  '''

  origin_point = []
  origin_point.append(point_2[0])
  origin_point.append(point_1[1])
  
  print(f"{origin_point[1]} - {point_2[1]} = {origin_point[1] - point_2[1]}")
  print(f"{origin_point[0]} - {point_1[0]} = {origin_point[0] - point_1[0]}")
  dist_a = abs(origin_point[1] - point_2[1])
  dist_b = abs(origin_point[0] - point_1[0])
  
  return math.sqrt(math.pow(dist_a, 2) + math.pow(dist_b, 2))

if __name__ == "__main__":
  point_1_x = int(sys.argv[1])
  point_1_y = int(sys.argv[2])
  
  point_2_x = int(sys.argv[3])
  point_2_y = int(sys.argv[4])
  print(f"Distance between ({point_1_x}, {point_1_y}) and ({point_2_x}, {point_2_y}) is {main([point_1_x, point_1_y], [point_2_x, point_2_y])}")
