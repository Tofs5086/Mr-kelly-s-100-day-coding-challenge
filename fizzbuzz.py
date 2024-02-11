for i in range(1,101):# code to print list of numbers from 1 -100
    if i%3 == 0 and i%5 == 0:# 1st condition, if a number is divisible by both 3 and 5 print fizzbuzz
        print('fizzbuzz')
    elif i%3 == 0:
        print('fizz')# 2nd condition, if a number is divisible by 3, print fizz
    elif i%5 == 0:
        print('buzz')#3rd condition, if a number is divisible by 5, print buzz
    else:
        print(i)
