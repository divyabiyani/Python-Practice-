import  cmath

a=float(input('Enter a:'))
b=float(input('Enter b:'))
c=float(input('Enter c:'))

d=(b*b)-(4*a*c)

sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)

print('The roots are {0} and {1}'.format(sol1,sol2))