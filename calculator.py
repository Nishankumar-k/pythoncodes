x = int(input(f'Enter the number 1: '))
y = int(input(f'Enter the number 2: '))
z = int(input(f'Enter the operator number: '))
if(z==1):
    print(x+y)
if(z==2):
    print(x-y)
if(z==3):
    print(x*y)
if(z==4):
    print(x/y) 
if(z>4):
    print(f"Invalid input for operator number")