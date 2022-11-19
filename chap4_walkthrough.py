import os
import pathlib

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# print(factorial(10))

# ---
# English Ruler
# ---

def draw_line(tick_length, tick_label=''):
    """Draw one line with given thick length 
    (followed by optional label)
    """
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(center_length):
    """Draw tick interval based on central tick 
    length
    """
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)
    
def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of 
    inches, major thick length
    """
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))

    
# print(draw_ruler(3, 2))


# ---
# Binary Search
# ---

def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of
    a python list.
    
    The search only considers the portion from data[low] to 
    data[high] inclusive.
    """
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid -1)
        else:
            return binary_search(data, target, mid + 1, high)


# search_list=[2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 22, 23, 24, 25, 26, 28, 30, 31, 32, 34, 36]
# print(binary_search(search_list, 36, 0, len(search_list)-1))


# ---
# Directory Disk Usage
# ---

def disk_usage(path):
    """Return the number of bytes used by a file/folder and
    any decendants
    """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            child = os.path.join(path, filename)
            total += disk_usage(child)

    print('{0:<7}'.format(total), path)
    return total


# work_dir = pathlib.Path('.').absolute()
# print(disk_usage(work_dir))


# ---
# Fibonacci
# ---

def bad_fibonacci(n):
    """Returns the nth fibonacci number"""
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)

# print(bad_fibonacci(20))

def good_fibonacci(n):
    """Returns pair of Fibonacci numbers 
    F(n) and F(n-1)
    """
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        return (a + b, a)

# print(good_fibonacci(20))


def linear_sum(S, n):
    """Return the sum of the first n numbers 
    of sequence S
    """
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]


# print(linear_sum([2, 3, 4, 5], 4))


def reverse(S, start:int, stop:int):
    """Reverse elements in implicit slice S[start:stop]"""
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        return reverse(S, start + 1, stop - 1)
    return S


# actual_list = [10, 30, 20, 50, 40, 70, 60, 90, 80,  1000]
# print(f"Actual list: -->  {actual_list}")
# print(f"Reversed list: --> {reverse(actual_list, 0, len(actual_list))}")


def power(x:int, n:int):
    """Compute the value x ** n for integer n"""
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
        


print(power(2, 10))
