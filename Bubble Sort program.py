
def Bubblesort(Arr):
    n= len(Arr)

    for fixtheindex in range(n-1,0,-1):
        for i in range(fixtheindex) :
            if Arr[i]>Arr[i+1] :
                temp=Arr[i]
                Arr[i]=Arr[i+1]
                Arr[i+1] = temp
        #print(Arr)

    
        
n = int(input().strip())
Arr = list(map(int, input().split()))



Bubblesort(Arr)

for i in range(n):
    print(Arr[i],end=" ")
