import math
def can(height,width,coverage):
    area=height*width
    no_of_cans=math.ceil(area/coverage)
    print(f'the number of cans needed is {no_of_cans}')

h = int(input('what is the height of the wall you want to paint? \n'))
w = int(input('what is the width of the wall you want to paint'))
c = 7
can(width=w,height=h,coverage=c)

