# write a function that takes two positional arguments and uses *args
# your function should:
"""
arguments:
    name: name of person
    job: job title of person
    *args: possesions that they own

returns --> Str
   It should return a string that says a nice message like
  "hello Gilad, I heard your job of washing dishes allows you to own a lawn-mower, house, cat, and bat"

Remember, your string needs to _grow_ with the *args - it needs infinite potential!

"""

def person_intro(name, job, *args):
  arg_str_msg=''
  for pos, arg in enumerate(args):
    if pos!=0:
      arg_str_msg +=', '
    if pos==len(args)-1 and pos!=0:
      arg_str_msg+='and '
    arg_str_msg+=arg
    
  return f"hello {name}, I heard your job of {job} allows you to own a {arg_str_msg}"
  
print(person_intro("Gilad", "washing dishes", "lawn-mower", "house", "cat", "bat"))