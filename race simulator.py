import random
print('enter number of players more than 3 and length of track')
num,length=map(int,input().split())
k=0

main=[]
for i in range (num):
    main.append([0])

j=0
for i in range(length//2+num+1):
    '''
    if i<num:
        for j in range(num):
            print('**')
    elif i>=num:
        for j in range(i):  #blank spaces in beginning
            print('##',end='')     #2 blank spaces
    '''
    if i<=length//2 :
        for j in range(num+1):  # for | | .... in beginning
            if j < num:
                print('\\ ',end='')
            else:
                if i==0:
                    print('iSi',end='')
                else:
                    print('|'+str(i%10)+'|',end='')
        
    if i<length:   # blank spaces in middle
        for j in range(length*2-i*4-3):
            print(' ',end='')
    
    if i>length//2:
        for j in range(num-k):
            print('\\ ',end='')
        for j in range(num-k):
            print('/ ',end='')
        k+=1

    if i<=length//2:
        for j in range(num+1):  # | | .. at end
            if i==0 :
                if j==0:
                    print('iFi',end='')
                else:
                    print(' /',end='')
            else:
                if j==0 and i<length//2:
                    print('|',(length-i)%10,'|',sep='',end='')
                elif i == length//2 and j==0:
                    print('',end='')
                else:
                    print(' /',end='')
    print()