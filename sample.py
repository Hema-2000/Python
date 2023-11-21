#__name__ variable is used to check that program is executed directly or executed from some other program
def f1():
    if __name__=="__main__":
        print("executed as an individual program")
    else:
        print("executed from another program")
f1()