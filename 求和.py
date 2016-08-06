largest=0
print'before',largest
for number in[3,6,9,12,66,88,990]:
    if number>largest:
        largest=number
print'after',largest

count=0
sum=0
for number in[33,11,22,44,55]:
    count=count+1
    sum=sum+number
print'count:',count,'sum:',sum

x=False
count=0
print'before',x
for number in[3,5,7,7,8,7,7,7,7,7,9]:
    if number==7:
        x=True
        count=count+1
print'after',x,'times:',count
