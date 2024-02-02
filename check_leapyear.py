year=int(input('enter the year you were born.'))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('you were born leap year')
        else:
            print('you were not born on a leap year')
    else:
        print('you were born on a leap year')
else:
    print('you were not born on a leap year')



