import sys
number = int(sys.argv[1])
def fizzbuzz(n):
    for num in range(1, n):
        if num % 2 == 0 and num % 3 == 0:
            print "FizzBuzz"
        elif num % 2 == 0:
            print "Fizz"
        elif num % 3 == 0:
            print "Buzz"
        else:
            print num
fizzbuzz(number)
