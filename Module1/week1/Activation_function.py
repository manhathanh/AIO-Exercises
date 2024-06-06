import math
e=math.e
α=0.01
# Check x is number
def is_number(x):
  try:
    float(x)
  except ValueError:
    return False
  return True
# Create activation function
def calc_activation_func(x,method):
  result=None
  if method=='sigmoid':
    result=1/(1+ pow(e,-x))
  elif method=='relu':
    if x<=0:
      result=0
    else:
      result=x
  elif method=='elu':
    if x<=0:
      result=α*(pow(e,x)-1)
    else:
      result=x
  return result
# Check activation function
def exercise():
    x=input('input x : ')
    if not is_number(x):
       print('x must be number')
       return exit()
    method = input('input method : ')
    x=float(x)
    result=calc_activation_func(x,method)
    if result == None:
       print(f'{method} is not supported')
    else:
       print(f'{method}: f({x}) = {result}')

exercise()



