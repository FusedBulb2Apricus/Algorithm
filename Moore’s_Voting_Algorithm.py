# This  alogorithm uses the technique of cancelling of one element with other if they are not equall.
#  it gives us the probable majority element in 1st step .
#  then in next step we check it that element is majority element or not.

def candidate(arr):
    count=1
    me= arr[0]

    i=1
    while i<len(arr):
        if arr[i]!= me:
            count-=1
            if count==0:
                me=arr[i]
                count=1
        else:
            count+=1
        i+=1
    return me

def IsMe(me,arr):
    n= (len(arr)+1)//2

    i=0
    c=0
    while i<len(arr):
        if arr[i]==me:
            c+=1
        if c==n:
            return me
        i+=1
    
    return None

arr= [2,2,1,1,1,2,2]
me= candidate(arr)

print(IsMe(me,arr))



