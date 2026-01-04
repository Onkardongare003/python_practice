# 1
# 2 2
# 1 2 3
# 4 4 4 4
# 1 2 3 4 5

for i in range(1,6,1):
    print()
    for j in range(1,i+1,1):
        if(i%2==0):
            print(i,end="")
        else:
            print(j,end="")


