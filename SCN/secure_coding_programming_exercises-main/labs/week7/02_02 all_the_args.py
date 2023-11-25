"""
Write a function that accepts the following arguments
INPUT:
    name: str
    job : str
    * args: adjectives (str) that describe things (i.e "happy", " sad")
    **args: possessions (str): value (int / float)
Output:
   Form a  nice string that explains everything relevant



example input:
   ('Gilad', 'teacher', 'happy', 'amazing', 'sooooo cool', bike = 2000, house = 1000, shoes = 20)
output:
   "Gilad is a teacher who is happy, amazing, and sooooo cool. Gilad has a bike worth 2000, a house worth 1000, and shoes with 20"


The string should accomadate any number of *args and **kwargs.
"""
def many_args(name:str,job: str,*args:str,**kwargs:int):
   
   # for the first part of the string
   adjectives = ", ".join(args)
   # for the second part of the string
   possessions = ", ".join([f"a {k} worth {v}" if k != 'shoes' else f" and {k} with a size {v}" for k, v in kwargs.items()])
   
   return f"{name} is a {job} who is {adjectives}. {name} has {possessions}"

print(many_args('Gilad', 'teacher', 'happy', 'amazing', 'sooooo cool', bike=2000, house=1000, shoes=20))