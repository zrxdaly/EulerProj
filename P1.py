#%% multiples of 3 and 5
# https://projecteuler.net/problem=1

a = 0
for i in range(1000):
    if (i%3 == 0 or i%5 == 0):
        a = a + i
print("The sum of multiples of 3 and 5 is %i", a)
# %%
