def foo():
    pass


try:
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ZArithmeticError")
except ArithmeticError:
    print("ArithmeticError")


foo()
