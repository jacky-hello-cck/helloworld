def func(x):
    if x == 1:
       def rv():
           print("x is equal to 1")
    else:
       def rv():
           print("x is not 1")
     
    return rv
new_func = func(2)
new_func()           
