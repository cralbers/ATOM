def convert(i, j, k):
    ''' (num, num, num) -> str

    Takes in the numbers i, j and k and
    returns a three digit number with the digits
    i j and k in order from greatest to least.
    '''

    if i >= j  and j >= k:
        return (str(i)+str(j)+str(k))
    elif i >= k and k >= j:
        return (str(i)+str(k)+str(j))
    elif j >= i and i >= k:
        return (str(j)+str(i)+str(k))
    elif j >= k and k >= i:
        return (str(j)+str(j)+str(k))
    elif k >= i and i >= j:
        return (str(k)+str(i)+str(j))
    elif k >= j and j >= i:
        return (str(k)+str(j)+str(i))
    elif k == 0 and i >= j:
        return (str(i)+str(j))
    elif j == 0 and i >= k:
        return (str(i)+str(k))
    elif j == 0 and k >= i:
        return (str(k)+str(i))
    elif i == 0 and k >= j:
        return (str(k)+str(j))
    elif k == 0 and j >= i:
        return (str(j)+str(i))
    elif i == 0 and j >= k:
        return (str(j)+str(k))
    elif k == 0 and j == 0:
        return str(i)
    elif k == 0 and i == 0:
        return str(j)
    elif i == 0 and j == 0:
        return str(k)





def
