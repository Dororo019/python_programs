# make the most simple class possible

class SimpleClass:

# create an instance of your SimpleClass and print it out
   
    def __str__(self):
        return "This is a simple class."

simple_instance = SimpleClass()
print(simple_instance)

# now add some functionality to your simple class

class LessSimpleClass:
    
# add one class attribute
    sales=0 

# add a class method
# @classmethod is a decorator that can be applied to a method within a class. 
# This transforms it into a class method, which means the method is bound to the class and not the instance of the class.

# It can be called on an instance and the class.
# When called on an instance, it will still receive the class as its first argument.
# It modifies a method to make it a class method. 
# A class method receives the class as an implicit first argument, just like an instance method receives the instance.
# It allows the method to be called on the class itself, rather than an instance of the class. 
# when you want a method that affects the class as a whole, not a specific instance of the class,jakkaltobea

    @classmethod
    def incr_sales(cls):
        cls.sales += 1
        print(f"Sales got incremented! Current sales: {cls.sales}")

# Print out the class attribute directly through the class
print(LessSimpleClass.sales)
# Create an instance of LessSimpleClass
instance = LessSimpleClass()

# print out your class attribute both from an instance of the class and through the class directly
print(instance.sales)
LessSimpleClass.incr_sales()
# run the method - both directly from the class and through an instance.
instance.incr_sales()
