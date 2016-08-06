smallest=None
for number in[22,1,44,55,76]:
    if smallest is None:
        smallest=number
    elif number<smallest:
        smallest=number
print'smallest',smallest

largest=None
for value in[1,23,33,56,34]:
    if largest is None:
        largest=value
    elif largest<value:
        largest=value
print'largest',largest
        

