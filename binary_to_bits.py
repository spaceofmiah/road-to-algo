    



def to_bit(val):
    """Takes any binary number and returns it's bit equivalent"""
    result = []
    while val >= 1:
        val, reminder = divmod(val, 2)
        result.append(str(reminder))
    
    result.reverse()
    return "".join(result)


for i in range(0, 128):
    print(to_bit(i))


    
