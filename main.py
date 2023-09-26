formula -n *(n-1)
formula- n *(n-1)
def fact_rec(n):
 if n==0 or n==1:
 return 1
 else:
return n*fact_rec(n-) 
number = int(input("enter a value:"))
res = fact_rec(number )
print("the factorial of {}is {}.". format(number, res))