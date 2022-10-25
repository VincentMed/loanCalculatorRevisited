# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:43:35 2022

@author: Vincent Medrano
"""
import numpy as np

class loan(object):
    def __init__ (self, name):  # initialize with a name, thie permits
                                # easier manamgement of multiple instances
        """
        loan is a class object to implement computations of 
        loan parameters
        
        name: documents the name associated with the instance of loan 

        Returns
        -------
        None.

        """
        #initialization
        self._name = name
        self._Principal = 0
        self._intAPR = 0
        self._Payment = 0
        self._nMonths=0
        
        
    def getName(self):
        print(f"\nName of loan: {self._name}")
    
    def getChoice(self):
        print("\nwhat would you like to compute?")
        print("Options: Payment, Principal, intAPR, nMonths")
        
        choice = 0
        
        while choice  not in ("Payment", "Principal", "intAPR", "nMonths"):
            choice = input("Enter choice... ")
            
        if choice == "Payment":
            self.computePmt()
        elif choice == "Principal":
            self.computePv()
        elif choice == "intAPR":
            self.compute_intAPR()
        else:
            self.compute_nMonths()


    def compute_intAPR(self):
        ''' Solve for interest rate, APR  '''
        self._Principal = float(input('Enter principal '))
        self._Payment = float(input('Enter payment '))
        self._nMonths = int(input('Enter number of months '))
        
        # The solution will be r where using Payment, n, and Principal works
        ## bisection algorithm finds the two sides of the equation are equal
        ## that is, the difference is 0
        ## side 1: Pmt*(1-(1+r)**(-n))
        ## side 2:  Pv*r
        
        #example of an in-line (lambda) function
        fIntRate = lambda r: self._Payment*(1-(1+r)**(-self._nMonths)) - self._Principal*r
        
        # low and high possible interest rates, APR
        # the actual rate is between 
        
        _rlow =0
        _rhigh = 50 
        
        _rl = _rlow/1200
        _rh = _rhigh/1200
        _count = 0
        
        while(_count < 20): # in case there is no solution
            _rTry = (_rl+_rh)/2
            if abs(fIntRate(_rTry)) < 0.001: break
            
            if fIntRate(_rTry) > 0: _rl = _rTry
            else: _rh = _rTry
            
            _count += 1
            
        if(_count >=20):
            print("no solution: try again")
            print(f"interest rate APR is > {_rTry*1200:.2f}%") # convert back to APR
            rTry = None
        
        print(f"Interest rate = {_rTry*1200:.2f}")
        return _rTry*1200

    def computePmt(self):        
        self._intRate = float(input("Enter interest rate"))
        _r = self._intRate/1200
        
        self._Principal = float(input("Enter present value"))
        
        self._nMonths = int(input("Enter number of months"))
        
        self._Payment = float(_r*self._Principal/(1-(1+_r)**-self._nMonths))
        print(f"Payment is ${self._Payment: .2f}")        
        
    
    def compute_nMonths(self):
        self._Principal = float(input("Enter the principal"))
        
        self._Payment = float(input("Enter your payment amount"))
        
        self.intRate = float(input("Enter your interest rate"))
        
        _r = self.intRate/1200
        
        self._nMonths = -(np.log(1-((self._Principal * _r) / self._Payment)) / np.log(1+ _r))
                           
        print(f"{self._nMonths: .0f} months to pay off loan")
    
    def computePv(self):        
        self._Payment = float(input("Enter your payment amount"))
        
        self.intRate = float(input("Enter your interest rate"))
        
        self._nMonths = int(input("Enter number of months"))
        
        _r = self.intRate/1200
        
        self.Principal = self._Payment/_r *(1-(1+_r)**(-self._nMonths))
        
        print(f"Current principal is ${self.Principal: .2f}")


#####################################################################     
  
if __name__ == '__main__':
    
    testloan = loan(input("Please name this loan"))
    testloan.getName()
    
    testloan.getChoice()