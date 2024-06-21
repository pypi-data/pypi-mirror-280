#omgamganapathayenamaha
#omgamganapathayenamaha
#omgamganapathayenamaha
#omgamganapathayenamaha
#omgamganapathayenamaha
def mul(a, b, *args):
 prod = a * b
 for item in args:
  prod = prod * item
 return prod

def div(a, b):
 if b == 0:
  raise Exception('Division by Zero Exception')
 else:
  return a / b

if __name__ == "__main__":
 print(mul(1,2,3,4,5))
 print(mul(5,6))
 print(div(5,6))

