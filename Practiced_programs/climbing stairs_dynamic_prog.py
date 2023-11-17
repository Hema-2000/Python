#The problem of climbing stairs where you can take 1 or 2 steps at a time is a
# classic example that can be solved using dynamic programming.
def climb_stairs(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        ways=[0]*(n+1)
        ways[1]=1
        ways[2]=2
        for i in range(3,n+1):
            ways[i]=ways[i-1]+ways[i-2]
        return ways
n=int(input("enter the number of stairs to climb"))
res=climb_stairs(n)
print(f"there {res} ways to climb {n} stairs")