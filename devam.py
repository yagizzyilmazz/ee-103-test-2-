#Try Newton Raphson for cube root
x = int(input('What x to find the cube root of? '))
g= int(input('What guess to start with? '))
print('Current estimated cubed = ', g**3)
next_g = g - ((g**3-x)/(3*g**2))
print(' Next guess to try = ', next_g)