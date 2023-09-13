# Run some basic comparisons on basic integers and floating points

# what is bigger, a or b?
a = 2
b = 10
 
num_list =[a,b]
print("biggest number(a,b) is:",max(num_list))
# What is smaller , c or d?
c = 2.02
d = 2.01119999

num_list2 =[c,d]
print("smallest number(c,d) is:",min(num_list2))

# what is bigger e or f?
e = float("inf")
f = 12912912912091928312903713582043754302895723048957

num_list3 =[e,f]
print("Here, the biggest number from (e,f) is:",max(num_list3))

# are these equal?

g = 1.02020202020
i = 1.0202020202011111

print("ARE they (g,i) equal :", g==i)