#Author --> Bhushan Gawali
#GitHub username --> bhushanoff
#CodeChef username --> bhushanoff

#This code converts:
#JoHn TOm WiLLLIams to J. T. Williams
#tom Williams to T. Williams
#tom to Tom

print('how many times you\'ll input names ?')
t=int(input())
while t:
    print('Enter the name')
    string=input()
    count=0 #number of blank spaces
    for i in string:    #counting blank spaces
        if i==' ':
            count+=1
    if count==0:
        string.lower()
        print(string.capitalize())
        t-=1
        continue
    else:
        i=0
        while i<len(string):
            if i==0 :
                new=''
                new+=string[i]
                print(new.capitalize()+'. ',end='')
                while not string[i]==' ':
                  i+=1
                i+=1  #goes to character immediately after space
            elif string[i-1]==' ' and count>=1:
                new=''
                if count>1:
                    new+=string[i]
                    print(new.capitalize()+'. ',end='')
                    while not string[i]==' ':
                        i+=1
                    i+=1  #goes to character immediately after space
                    count-=1
                new=''
                while count==1 and i<len(string):
                    new+=string[i]
                    i+=1
                new.lower()
                print(new.capitalize())
        
    t-=1