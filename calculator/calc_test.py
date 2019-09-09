#!/usr/bin/env python

from calculator import Calculator

calc = Calculator()
'''basic add function'''
print ("1+1=", calc.add(1,1))
'''can add decimals'''
print("1.2+5=", calc.add(1.2, 5))

'''SUBTRACT'''
'''basic'''
print("13-7=", calc.subtract(13,7))
'''can subtract decimals'''
print("64.2-8.1=", calc.subtract(64.2, 8.1))

'''MULTIPLY'''
print("3*6=", calc.multiply(3,6))
print("9*0.5=", calc.multiply(9, 0.5))

'''DIVIDE'''
print("6/3=", calc.divide(6,3))
'''check for divide by 0 error handling'''
print("9/0=", calc.divide(9,0))

'''check for invalid operator input in interactive mode'''

calc.main()

'''TODO in calculator.py
--Add a print_globals function (for testing), and a set_globals private function
--in eval_operation clean up how the computation is printed up
'''
