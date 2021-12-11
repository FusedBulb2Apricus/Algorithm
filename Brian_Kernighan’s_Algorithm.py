# subtracting 1 from a decimal number flips alll the bits after the rightmost 
# set bit (which is 1) including the rightmost bit
# 10 = 00001010
# 9  = 00001001
# So if we subtract a number by 1 and do it's bitwise & with itself (n&(n-1)) , it will
# unset the rightmost bit 
# so If we do the upper step again and again it wiil take t times to become the n = n&(n-1) to become 0
# where the 1 is the number of the 1 in the bits
# 
#  
# n= binary form of n
def CountOne(n):
    c=0
    while n>0:
        c+=1
        n=n&(n-1)
    return c


# 00000000000000000000000000001011 == 11
n= 11
print(CountOne(n))
