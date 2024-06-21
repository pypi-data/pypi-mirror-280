#omgamganapathayenamaha
#omgamganapathayenamaha
#omgamganapathayenamaha
#omgamganapathayenamaha
#omgamganapathayenamaha
def add(a, b, *args):
 l = [a, b]
 l.extend([item for item in args])
 return sum(l)

def sub(a, b):
 return a - b

if __name__ == "__main__":
 print(add(1,2,3,4,5))
 print(add(5,6))
 print(sub(5,6))

