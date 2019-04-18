import cmath


def add_complex_numbers(real_num1, imaginary_num1, real_num2, imaginary_num2):
    complex_1 = complex(real_num1, imaginary_num1)
    complex_2 = complex(real_num2, imaginary_num2)
    sum = complex_1 +complex_2
    return sum
def subtraction(a1,b1,a2,b2):
    c1 = complex(a1,b1)
    c2 = complex(a2, b2)
    difference = c1-c2
    return  difference
def division(a1,b1,a2,b2):
    c1 = complex(a1,b1)
    c2 = complex(a2, b2)
    quet = c1-c2
    return  quet

def getinput():
    print("Real:")
    a1 = float(input())
    print("Imaginary:")
    b1 = float(input())
    return a1,b1
def operation():
    print("1:Addition")
    print("2:subtraction")
    print("3:Multiplication")
    print("4:Division")
    print("5:Inversion")
    print("6:Negation")
    print("press any key for exit")

    on = True
    while on:
        op = input()
        op = int(op)
        if op==1:
            a1,b1 = getinput()
            a2, b2 = getinput()
            print("sum ="+str(addition(a1,b1,a2,b2)))
        elif  op==2:
            a1, b1 = getinput()
            a2, b2 = getinput()
            print("Difference ="+str(subtraction(a1,b1,a2,b2)))
        elif  op==3:
            a1, b1 = getinput()
            a2, b2 = getinput()
            print("product ="+str(multiplication(a1,b1,a2,b2)))
        elif op==4:
            a1, b1 = getinput()
            a2, b2 = getinput()
            print("quetient ="+str(devision(a1, b1, a2, b2)))

        elif op==5:
            a1,b1 = getinput()
            print("inversion ="+str(inversion(a1, b1)))

        elif op==6:
            a1, b1 = getinput()
            print("Negation ="+str(negation(a1,b1)))

        else:
            on = False
