def info_person(*args,**kwargs,):
    for key,values in kwargs.items():
        print(key,values)

    print(args)
info_person(1,2,3,name='Tobi,', age=30,dept='ENG')
info_person(5086,name='tofs', age=23,dept='BIO')

