#Program that prints the numbers from 1 to 100 .
#multiples of three print "Fizz"
#multiples of five  print "Buzz"
#multiples of three & five  print "FizzBuzz"
num=0

while (num<100):
    num+=1
    if(num%3==0 and num%5==0):
        print("FizzBuzz")
    elif(num%3==0):
        print("Fizz")
    elif(num%5==0):
        print("Buzz")
    else:
        print(num)
    
