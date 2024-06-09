import math
import random

# factorial function

def factorial(y):
  x=1
  for i in range(1,y+1):
    x=x*i
  return x
factorial(5)

# function ham so

def sin_(x,n):
  sin_approx = 0
  
  for z in range(0,n):
    coef=(-1)**z
    num=x**(2*z+1)
    denom=factorial(2*z+1)
    sin_approx=sin_approx+(coef*(num/denom))
  return print(f'{sin_approx:.4f}')

def cos_(x,n):
  cos_approx = 0
  
  for z in range(0,n):
    coef=(-1)**z
    num=x**(2*z)
    denom=factorial(2*z)
    cos_approx=cos_approx+(coef*(num/denom))
  return print(f'{cos_approx:.2f}')

def sinh_(x,n):
  sinh_approx = 0
  
  for z in range(0,n):
    coef=1
    num=x**(2*z+1)
    denom=factorial(2*z+1)
    sinh_approx=sinh_approx+(coef*(num/denom))
  return print(f'{sinh_approx:.2f}')

def cosh_(x,n):
  cosh_approx = 0
  
  for z in range(0,n):
    coef=1
    num=x**(2*z)
    denom=factorial(2*z)
    cosh_approx=cosh_approx+(coef*(num/denom))
  return print(f'{cosh_approx:.2f}')

sin_(3.14,10)
cos_(3.14,10)
sinh_(3.14,10)
cosh_(3.14,10)