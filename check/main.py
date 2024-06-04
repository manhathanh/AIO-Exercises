def factorial(n):
  x=1
  for i in range(1,n+1):
    x=x*i
  return x

def multi(a,b):
  return a*b




if __name__=="__main__":
  print(f"factorial: {factorial(5)}")