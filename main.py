def complete_bracelet(a):
n = len(a)
k = 2
while k*k <= n:
    if n % k == 0:
        m = n // k
        if a[:m]*k==a or a[:k]*m==a:
            return True
    k += 1
return False