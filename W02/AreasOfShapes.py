import math

CONVERT_SQUARE_METERS = 1/10000

length_of_side = float(input('What is the length of a side of the square (centimeters)? '))
square_area = length_of_side ** 2

print(f'The area of the square is: {square_area:.2f}, cm2 1{square_area * CONVERT_SQUARE_METERS}') 

# length_of_rectangle = float(input('What is the length of rectangle? '))
# length_of_width = float(input('What is the width of the rectangle? '))
# rectangle_area = length_of_rectangle * length_of_width
# print(f'The area of the rectangle is: {rectangle_area:.2f}')

# radius_of_circle = float(input('What is the radius of the circle? '))
# circle_area = (radius_of_circle ** 2) * math.pi
# print(f'The area of the circle is {circle_area:.2f}')

# length_value = float(input('Please, write a length: '))
# area = length_value ** 2
# circle_area = (area ** 2) * math.pi
# sphere = (4 / 3) * math.pi * (length_value ** 3)
# cube = length_value ** 3
# print(f'The area of the square is: {area} ')
# print(f'The area of the circle is: {circle_area:.2f}')
# print(f'The volume of the sphere is: {sphere:.2f}')
# print(f'The volume of the cube is: {cube}')