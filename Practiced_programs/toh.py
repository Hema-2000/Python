def toh(n,s,d,t):
    if(n>0):
        toh(n-1,s,t,d)
        print(f"moivng {n} from {s} to {d}")
        toh(n-1,t,d,s)

toh(2,'source','destination','temp')
def add(a,b):
    return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b