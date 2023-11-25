## fix the code below so it runs correctly


def args(*args):
    for a in args:
        print(a + 2)


my_list = [1,23,123,12,32,2,32,32,]

## this code is broken
args(*my_list)

# fix it ^^^ so it works.  Fixed it with *unpacking operator and to look more neat made the list in on line
