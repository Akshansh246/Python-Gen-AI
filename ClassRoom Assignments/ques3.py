a = int(input('Enter first Term :'))
d = int(input('Enter common difference :'))
n = int(input('Enter term number :'))

# formula to find the nth term
an = a + (n-1) * d
print("The first n-terms are : ",an)
#sum of  first n-terms
sn = n/2 * (a + an)
print("The sum of first n-terms are : ",sn)
