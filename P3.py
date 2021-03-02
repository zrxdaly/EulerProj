#%% Largest prime factor
# https://projecteuler.net/problem=3

# input a number
a = int(input("please enter an integer number, this program will output largest prime number"))

def prime(a):
    for i in range(2,int(a/2)+1):
        if a%i == 0:
            return(False)
    return(True)

try:
    for i in range(2,a):
        if a%i == 0:
            if prime(int(a/i)):
                print("The largest prime number of input value is %i"%int(a/i))
                break
except:
    print("The format of input value is not correct")

# %%
