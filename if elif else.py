print('Hello world')

x=float(input('What is your weight ? '))
y=input('k(kg) or l(lbd)')
if y.upper() == 'K':
    c=x/0.45
    print(f'Your weight is {c} lbs')
else:
    c=x*0.45
    print(f'Your weight is {c} kg')
