# 1. Implement the program to print true when the first and last element in the list was even, else print false.
numlist=[2,4,5,6,7,8]
if numlist[0]%2==0 and numlist[len(numlist)-1]%2==0:
    print(True)
else:
    print(False)


# ---------------------------------------------------------------------------------------------------------------
# 2) implement the program to create a function which performs the count method. Without using any methods.

numlist=[1,2,2,3,3,3,4,5,6,6,6,7,7,8]
target_element=int(input("enter an item in list : "))
def counting_num(numlist,target_element):
     count=0
     for item in numlist:
        if item==target_element:
           count+=1
     return count
result=counting_num(numlist,target_element)
print(f"the element {target_element} appeared {result} times in list")

# --------------------------------------------------------------------------------------------------------------------------

# 3) write a program to print the prime numbers in the new list from the existing list.
numlist=[2,3,4,5,7,9,13,19]
primelist=[]
for ind in range(0,len(numlist),1):
    fact=0
    number=numlist[ind]
    for i in range(1,number+1,1):
        if number%i==0:
            fact+=1
    if fact==2:
     primelist.append(number)
print("primelist : ", primelist)


