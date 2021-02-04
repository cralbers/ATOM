def hello(s):
    ''' '''
    print('Hello, ' + s + '.')
    return None


def ciao(s):
    ''' '''
    print('Ciao, ' + s + '.')
    return None

def greeting(f, s):
    f(s)
    print('Calling ' + f.__name__)
    return None
