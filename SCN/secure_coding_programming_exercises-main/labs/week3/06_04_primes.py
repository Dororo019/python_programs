# Exercise

# Write a python program to print all prime numbers between 0 to 100 , and print how many prime numbers are there
# if you don't know an algorithm to check for primes
# ask Dr. Kurunandan Sir
# google it

for num in range(0,100):
    if all(num%i!=0 for i in range(2,num)):
        print (num)
        