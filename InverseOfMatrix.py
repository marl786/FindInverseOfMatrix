def inverse(l):
    
    nl=list(range(len(l)))
    for x in range(len(nl)):
        nl[x]=list(range(len(nl)))


    for x in range(len(nl)):
        for y in range(len(nl[x])):
            nl[x][y]=0.0


    for x in range(len(nl)):
        nl[x][x]=1


    count=0
    found=False
    while count<=len(l) and found==False:
        if l[count][0]!=0:
            found=True
        count=count+1
    if found==False:
        nl="ERROR"
    else:
        temp=l[count-1]
        l[count-1]=l[0]
        l[0]=temp

        temp=nl[count-1]
        nl[count-1]=nl[0]
        nl[0]=temp


        for own in range(len(l)):
            divider=l[own][own]
            for x in range(len(l)):
                l[own][x]=l[own][x]/divider
                nl[own][x]=nl[own][x]/divider
            for row in range(len(l)):
                if row!=own:
                    divider=l[row][own]
                    for x in range(len(l)):
                        l[row][x]=l[row][x]-divider*l[own][x]
                        nl[row][x]=nl[row][x]-divider*nl[own][x]

    return nl
q=int(input("Please enter the number of rows or columns in the Matrix: "))
d=list(range(q))
for w in d:
    d[w]=list(range(q))
    for e in range(q):
        d[w][e]=float(input(f'Please enter row number {w} column number {e}: '))

def det(A):
    ans=0
    if len(A)==2:
        return(A[0][0]*A[1][1])-(A[0][1]*A[1][0])
    else:
        for x in range(len(A)):
            nl=list(range(len(A)-1))
            for z in range(1, len(A)):
                rl=list()
                for y in range(len(A)):
                    if y!=x:
                        rl=rl+[A[z][y]]
                nl[z-1]=rl
            if x%2==0:
                ans=ans+(A[0][x]*det(nl))
            else:
                ans=ans+(-A[0][x]*det(nl))
        return ans
x=det(d)

print(f'The Determinant is {x} hence:')
if x==0:
    print("INVERSE DOES NOT EXIST")
else:
    print("YOU MAY PROCEED")
    z=inverse(d)
    if z!="ERROR":
        for y in z:
            print(y)
    else:
        print("INVERSE DOES NOT EXIST")
