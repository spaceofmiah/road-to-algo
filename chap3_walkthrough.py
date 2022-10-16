
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

# print(prefix_average3([10,2,3,5,60]))


# ---
# Three-Way Set Disjointness
# ---


def disjoint1(A, B, C):
    """Return True if there is no element common to all three lists."""
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True



# ---
# Asymptotic Analysis
# ---

def disjoint2(A, B, C):
    """Return True if there is no element common to all three lists."""
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    return True


# ---
# Element Uniqueness
# ---

def unique1(S):
    """Return True if there are no duplicate element in sequence S"""
    for j in range(len(S)):
        for k in range(j + 1, len(S)):
            if S[j] == S[k]:
                return False
    return True


# ---
# Sorting as a Solver
# ---

def unique2(S):
    """Return True if there are no duplicate element in sequence S"""
    temp = sorted(S)
    for j in range(1, len(temp)):
        if S[j - 1] == S[j]:
            return False
    return True


