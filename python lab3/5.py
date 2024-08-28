import statistics

list=[1,2,3,4,5,3,3,4,7,9]

list.sort()
mean=sum(list)

if(len(list)%2==0):
    index=(int)(len(list)/2)
    median=(list[index]+list[index+1])/2
else:
    index=(len(list)+1)/2
    median=list[index]


mode=statistics.mode(list)

print("median: ",median)
print("mean: ",mean)
print("mode: ",mode)