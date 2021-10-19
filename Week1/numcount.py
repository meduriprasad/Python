#/usr/bin/python3
def countDigit(n):
    if n/10 == 0:
        return 1
    return 1 + countDigit(n // 10)
 
 
# Driver Code
n = 345289467
print("Number of digits : % d" % (countDigit(n)))