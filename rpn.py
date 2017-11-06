#!/usr/bin/env python3
import operator
import readline
from termcolor import colored, cprint
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def calculate(arg):
    stack =  list()
    for token in arg.split():
        try:
            stack.append(int(token))
        except ValueError:
            try :
                arg2 = stack.pop()
                arg1 = stack.pop()
                function = ops[token]
                #print("here1\n")
                result = function(arg1,arg2)
                #print("here2\n")
                stack.append(result)

            except ArithmeticError:
                #print("Improper Arithmetic")
                cprint("Improper Arithmetic","yellow")
                return -1

            except:
                print("Improper use of calculator")
                return -1

    print(stack)
    return stack.pop()

def main():
    while True:
        calculate(input("rpn calc> "))

if __name__ == '__main__':
    main()
