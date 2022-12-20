import math
def paint_calc(height,width,cover):
    return math.ceil(height*width/5)

test_h = int(input("Height of wall: "))
test_w = int(input("Width of walll: "))
coverage = 5

print(f"You will need {paint_calc(height = test_h,width=test_w,cover=coverage)} cans of paint!")