#!/usr/bin/env python		
'''#Basic four function calculator program with user input
	Author:Jay Spendlove
	Program Name: Calculator
	email:jayclark24@gmail.com

	'''

class Calculator (object):

    gOperation=0
    gNum1=0
    gNum2=0
    
    
    
    def main(self):
        '''Main function to put all the pieces together, and execute inside a while loop'''
        
        
        #print(add(1,2))
        
        calculate = True
        print(calculate)
        
        print("Hi! Welcome to Jay's Calculator!")
                   
        
        while (calculate):
            
            self.gOperation =0
            self.gNum= 0
            self.gNum2 = 0
            
            print("Continue calculating? [y / n]")
            
            if (input() == 'n'):
                calculate = False
            else:
                self.initialize_globals()
            
                self.eval_operation()
                print("end of loop")
        return
    

    '''______________________________________________________________'''
    def add (self,num1, num2):	
        '''function to compute the sum of two numbers'''

        return num1 + num2

    '''________________________________________________________________'''
    def subtract(self, num1, num2):
        '''function to subtract 2 numbers'''

        return num1 - num2

    '''___________________________________________________________________'''
    def multiply(self, num1, num2):
        '''function to multiply 2 numbers'''

        return num1*num2

    '''______________________________________________________________'''
    def divide (self, num1, num2):
        '''function to divide 2 numbers'''

        return num1/num2


    '''_______________________________________________________________'''
    def ask_operation(self):
        '''function to recieve user input for specific operation'''


        operation = input('Please select operation - \
                            1. Add \
                            2. Subtract \
                            3. Multply \
                            4. Divide \
                                      ')

        return operation
    

    '''__________________________________________________________________'''
    def ask_num(self):
        '''function to recieve user input for specific numbers'''
        num = input('Enter number:')
        return num

    
    '''_____________________________________________________________________'''
    def initialize_globals(self):
        '''Function to initialize global variables with operations ask_operation() and ask_num()'''
        self.gOperation = self.ask_operation()
        self.gNum1 = self.ask_num()
        self.gNum2 = self.ask_num()
        
        print("gOperation is ", gOperation, " and gNum1 and gNum2 are ", gNum1, " & ", gNum2)

        return

    '''_____________________________________________________________________________'''
    def eval_operation(self):
        '''Function to do the computations with the inputted operation and numbers,
            and to test for 2 specific errors of 1) bad input for operation, and 
            2) divide by 0 error'''

        if(gOperation == 1):
            print(gNum1, " + ", gNum2, " = ",
                    self.add(gNum1, gNum2))
        elif (gOperation == 2):
            print(gNum1, " - ", gNum2, " = ",
                    self.subtract(gNum1, gNum2))
        elif (gOperation == 3):
            print(gNum1, " x ", gNum2, " = ",
                    self.multiply (gNum1, gNum2))
        elif (gOperation == 4):
            if(gNum2 == 0):
                print('Divide by 0 error')
            else:
                print(gNum1, " / ", gNum2, " = ",
                    self.divide(gNum1, gNum2))
        else:
            self.gOperation = 0
            print ('error')
        
        return
    
    
    '''_________________________________________________________________________________________'''
    

    
c1 = Calculator()
c1.main()
            
        
        



