def is_multiple(n, m):
    """Returns True if n is a multiple of m"""
    counter, flag = 1, True
    while True:
        result = counter * n

        # result greater than the multiple `m`, signifies `n` is not a factor
        if result > m:
            flag = False
            break
        
        # check result equality
        flag = True if result == m else False
        if flag == True: break
        counter += 1

    return flag


def is_even(k):
    """Returns True if k is even and False otherwise"""
    return True if divmod(k, 2)[-1] == 0 else False
