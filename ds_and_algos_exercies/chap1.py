from typing import List, Optional, Tuple


def is_multiple(n:int, m:int) -> bool:
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


def is_even(k:int) -> bool:
    """Returns True if k is even and False otherwise
    
    constraint:
    -----------
    Cannot use the multiplication, modulo, or division operators
    """
    return True if divmod(k, 2)[-1] == 0 else False


def compare(seq:list, old_min:int, old_max:int) -> Tuple[int, int]:
    """Compares old minimum & maximum value with the next element
    in the sequence 
    """
    if len(seq) == 0:
        return old_min, old_max
    
    if len(seq) == 1:
        return (
            seq[0] if seq[0] < old_min else old_min, # compare sequence last element with prev old min
            seq[0] if seq[0] > old_max else old_max  # compare sequence last element with prev old max
        )

    old_min, old_max = (seq[0] if seq[0] < old_min else old_min, seq[0] if seq[0] > old_max else old_max)
    return compare(seq[1:], old_min, old_max)


def minmax(seq:list) -> Tuple[int, int]:
    """Returns the smallest and largest numbers
    
    constraint: 
    -----------
    Do not use the built-in functions min or max in implementing your solution.
    
        personal added constraint:
        **************************
        Do not use any built-in sort method/function

        implementation would be very simple using any built-in function e.g

            new_seq = sorted(seq)
            return new_seq[0], new_seq[-1]
    """
    new_seq = seq
    return compare(new_seq[1:], new_seq[0], new_seq[0])
    

def number_squares_below_n(n:int, just_odd:Optional[bool]=False) -> List:
    """returns a list of squares of intergers lesser than `n`
    
    parameters
    ==========
    just_odd <bool> [default: False]
        when True returns squares all the odd positive integers
        lesser than `n`
    """
    return [ i*i for i in range(1, n, 2) ] if just_odd else  [ i*i for i in range(n) ]


def sum_squares(n) -> int:
    """returns the sum of the squares of all the positive 
    integers smaller than `n`

    Requirements:
    -------------
    Give a single command that computes the sum
    """
    return sum(number_squares_below_n(n, just_odd=False))


def sum_odd_squares(n) -> int:
    """returns the sum of the squares of all odd positive 
    integers smaller than `n`

    Requirements:
    -------------
    Give a single command that computes the sum, relying 
    on Python’s comprehension syntax and the built-in sum 
    function.
    """
    return sum(number_squares_below_n(n, just_odd=True))


def custom_reverse(data:list):
    """Reverses a list element to the opposite direction"""
    return data[::-1]


def odd_product_pair(data:list) -> bool:
    """takes a sequence of integer values and determines 
    if there is a distinct pair of numbers in the 
    sequence whose product is odd.
    """
    counter = len(data) - 1
    directory = {}

    while counter >= 0:
        cur_val = data[counter]
        for idx, value in enumerate(data):
            if idx == counter: continue
            if divmod(value * cur_val, 2)[-1] == 1:
                if (value, cur_val) in directory or (cur_val, value) in directory: continue
                directory[(value, cur_val)] = True
        counter-=1
    
    return True if any(directory.values()) else False

