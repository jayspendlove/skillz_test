#!/usr/bin/env python		
'''#Basic four function calculator program with user input
	Author:Jay Spendlove
	Program Name: Calculator
	email:jayclark24@gmail.com

	'''

class Calculator (object):
	
	def main(self):
		'''Main function to put all the pieces together, and execute inside a while loop'''
		calculate = True;
		print (calculate)

        
        	print("Hi! Welcome to Jay's Calculator!") 
        
        	while (calculate):

			self.__init__()
			res = raw_input("COntinue?")
			print("gobble-dee-gook")
            		if (res  == 'n'):
                		calculate = False
            		else:
                		self.initialize_globals()
            
                		self.eval_operation()
                	print("end of loop")
        	return
	

	def __init__(self):
                '''Initializes global variables to 0'''


		global gOperation
        	global gNum1
        	global gNum2
                self.gOperation=0
                self.gNum1=0
                self.gNum2=0    
    		return


	def add (self,num1, num2):	
        	'''function to compute the sum of two numbers'''

        	return num1 + num2

	def subtract(self, num1, num2):
        	'''function to subtract 2 numbers'''

        	return num1 - num2

	def multiply(self, num1, num2):
        	'''function to multiply 2 numbers'''

        	return num1*num2

	def divide (self, num1, num2):
        	'''function to divide 2 numbers'''

        	return num1/num2

	def ask_operation(self):
        	'''function to recieve user input for specific operation'''


        	operation = input('Please select operation - \
                            1. Add \
                            2. Subtract \
                            3. Multply \
                            4. Divide \
                                      ')

        	return operation

	def ask_num(self):
        	'''function to recieve user input for specific numbers'''
        	num = input('Enter number:')
        	return num

	def initialize_globals(self):
        	'''Function to initialize global variables with operations ask_operation() and ask_num()'''
        	self.gOperation = self.ask_operation()
        	self.gNum1 = self.ask_num()
        	self.gNum2 = self.ask_num()

        	###print("gOperation is ", gOperation, " and gNum1 and gNum2 are ", gNum1, " & ", gNum2)

        	return

	def eval_operation(self):
        	'''Function to do the computations with the inputted operation and numbers,
            	and to test for 2 specific errors of 1) bad input for operation, and 
            	2) divide by 0 error'''

        	if(self.gOperation == 1):
            		print(self.gNum1, " + ", self.gNum2, " = ",
                    	self.add(self.gNum1, self.gNum2))
        	elif (self.gOperation == 2):
            		print(self.gNum1, " - ", self.gNum2, " = ",
                    	self.subtract(self.gNum1, self.gNum2))
        	elif (self.gOperation == 3):
            		print(self.gNum1, " x ", self.gNum2, " = ",
                    	self.multiply (self.gNum1, self.gNum2))
        	elif (self.gOperation == 4):
            		if(self.gNum2 == 0):
                		print('Error: Divide by 0')
            		else:
                		print(self.gNum1, " / ", self.gNum2, " = ",
                    		self.divide(self.gNum1, self.gNum2))
        	else:
            		self.gOperation = 0
            		print ('Error: Invalid Operator')

        	return

