#Author --> Bhushan Gawali
#Github Username --> bhushanoff
#CodeChef Username --> bhushanoff

#this code rewrites the numerical input adding commas
#indicating thousands,millions,etc.

def comma(num):
    other_num=num.copy()
    x=len(other_num)
    count=x//3   #number of commas we need
    j=1
    while j<=count:
        other_num.insert(x-3*j,',')
        j+=1
    return other_num

print('how many numbers you want to enter ?')
t=int(input())
for i in range(t):
    print('enter the number')
    num=list(input())
    print("".join(comma(num)))