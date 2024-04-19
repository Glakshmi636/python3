n=int(input())

space=n-1
stars=1

for i in range(n):
    for j in range (space):
        print(" ",end="")
        
    for j in range(stars):
        print(j+1,end="")
    print()
    
    space=space-1
    stars=stars + 1
