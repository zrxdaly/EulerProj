#%% sum of even value terms in Fibonacci sequence
# https://projecteuler.net/problem=2

a1 = 1
a2 = 2
a2_sum = a2
while a2 < 4000000:
    a1, a2 = a2, a1+a2
    # alternative 
    # a3 = a1 + a2
    # a1 = a2
    # a2 = a3

    if a2%2 == 0:
        a2_sum = a2_sum + a2

print("The sum of even-value in Fibonacci number is %i", a2_sum)
# %%
