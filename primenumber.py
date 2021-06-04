low = 1
high = 100
print('the prime number in between ',low,' and ',high,' are: ')
for num in range(low,high+1):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)