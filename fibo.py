#using a loop to generate fibonacci
def F(n):
    a,b=1,1 
    for x in range(n-1):
    		a,b=b,a+b
    return a	
print F(5)