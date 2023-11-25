def person_intro(name, job, *args):
  message_possessions = ', '.join(args[:-1]) + ', and ' +args[-1] if args else ''
    
  return f"hello {name}, I heard your job of {job} allows you to own a {message_possessions}"
  
print(person_intro("Gilad", "washing dishes", "lawn-mower", "house", "cat", "bat"))

def person_intro(name, job, *args):
    arg_str_msg = ''
    for pos, arg in enumerate(args):
        if pos != 0:
            arg_str_msg += ', '
        if pos == len(args) - 1 and pos != 0:
            arg_str_msg += 'and '
        arg_str_msg += arg
    return f"Hello {name}, I heard your job of {job} allows you to own a {arg_str_msg}."

print(person_intro("Gilad", "washing dishes", "lawn-mower", "house", "cat", "bat"))
