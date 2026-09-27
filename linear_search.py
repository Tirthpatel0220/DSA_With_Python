array=[10,20,30,40,50,60]
target=1

def linear_search(array,target):
    for i in range(len(array)):
        if array[i]==target:
            return i
    else:
        return -1

result=linear_search(array,target)
print(result)