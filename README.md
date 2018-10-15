# Maths
Created a program to find and print the prime numbers which occur till the given value of 'n'.
First I have created a Boolean array having True values only for 'n' numbers.
Since we know if a number(say a) has factors then definitely one of its factor will lie from 1 to √a , that's why I have put that condition on while loop.
Now , since I know 2 is prime then definitely its multiple will not be prime,therefore changing the values of the multiples of 2 from True to False in Boolean Array.
Now the first 'if condition' used in while loop is to check whether the value is True or False,if True then change its multiples values from True to False in the Boolean Array.
After doing this all, I have used the range function with for to print all those numbers which have True Value in Boolean Array.
Its complexity is :  O((√n)log(log(n)))
