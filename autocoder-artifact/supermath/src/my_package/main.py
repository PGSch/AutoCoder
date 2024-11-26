if __name__ == '__main__':
    import sys
    from . import add, subtract, multiply, divide

    a, b = map(float, sys.argv[1:3])
    print('Add:', add(a, b))
    print('Subtract:', subtract(a, b))
    print('Multiply:', multiply(a, b))
    print('Divide:', divide(a, b))
