
# ---
# Quadratic-Time Algorithm
# ---

def prefix_average1(S):
    """Return list such that, for all j, A[j] equals average of S[0],,,,,S[j]"""
    n = len(S)
    A:list = [0] * n

    for j in range(n):
        total = 0

        for i in range(j + 1):
            total += S[i]
        
        A[j] = total / (j + 1)

    return A


# print(prefix_average1([10,2,3,5,60]))


# ---
# Asymptotic Analysis
# ---

def prefix_average2(S):
    """Return list such that, for all j, A[j] equals average of S[0],,,,,S[j]"""
    n = len(S)
    A:list = [0] * n

    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j+1)
    
    return A

# print(prefix_average2([10,2,3,5,60]))


# ---
# A Linear-Time Algorithm
# ---

def prefix_average3(S):
    """Return list such that, for all j, A[j] equals average of S[0],,,,,S[j]"""
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j + 1)
    return A

print(prefix_average3([10,2,3,5,60]))
