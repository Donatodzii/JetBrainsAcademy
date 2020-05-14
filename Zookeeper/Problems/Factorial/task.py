N = int(input())
fact_n = 1
if N == 1 or N == 0:
    print(fact_n)
while N:
    fact_n *= N
    N -= 1
print(fact_n)
