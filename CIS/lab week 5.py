def letterhead(name):
    x = '*'
    y = len(name)

    print((x*y)+(10*x))
    print()


def letterhead2(name):
    x = '*'
    y = len(name)
    

    print('{:*^30}' .format(''))
    print('{:*^30}' .format(name))
    print('{:*^30}' .format(''))
