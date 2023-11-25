# recreate your previous generator from 01, but use a generator expression


my_gen = (num for num in range(2,11) if num%2==0)  # fill out the code to make it work!


# practice using your generator
for i in my_gen:
    print(i)


print("second run!")
print()
# does it work two times? no
for i in my_gen:
    print(i)
