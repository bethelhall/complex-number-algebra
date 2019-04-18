import cmath


def add_complex_numbers(real_num1, imaginary_num1, real_num2, imaginary_num2):
    real_num1 = eval(input("Enter the first real number: "))
    imaginary_num1 = eval(input("Enter the first imaginary number"))
    real_num2 = eval(input("Enter the second real number: "))
    imaginary_num2 = eval(input("Enter the second imaginary number: "))
    complex_1 = complex(real_num1, imaginary_num1)
    complex_2 = complex(real_num2, imaginary_num2)

    real1 = complex_1.real
    real2 = complex_2.real

    imaginary1 = complex_1.imag
    imaginary2 = complex_2.imag

    real_sum = real1 + real2
    imag_sum = imaginary1 + imaginary2

    result = complex(real_sum, imag_sum)
    return result

def inversion(number):
    mul_inv = 1 / number        
    return mul_inv

def negation(number):
    negated = -number
    return negated

def multiplication(first_number, second_number):
    mul = first_number * second_number
    return mul

def main():
    print("testing")
    print("The result is: ", add_complex_numbers(2, 2, 3, 3))


if __name__ == '__main__':
    main()
