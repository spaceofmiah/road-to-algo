

class Vector:
    """Represents a vector in a multidimensional space."""

    def __init__(self, d) -> None:
        """Creates a d-dimensional vector of zeros"""

        self._coords = [0] * d
    
    def __len__(self):
        """Returns the dimension of the vector"""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector"""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Return jth coordinate of vector"""
        self._coords[j] = val
    
    def __add__(self, other) -> "Vector":
        """Return sum of two vectors"""
        if len(self) != len(other):
            raise ValueError("Dimension must be same")
        
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        
        return result

    def __eq__(self, other: "Vector") -> bool:
        """Returns True if vector has same coordinate as other"""
        return self._coords == other._coords

    def __ne__(self, other: "Vector") -> bool:
        """Returns True if vector differs from others"""
        return not self == other

    def __str__(self) -> str:
        """Produce string representation of vector"""
        return '<' + str(self._coords)[1:-1] + '>'


def vector_check():
    """Experiment with custom Vector class"""
    v = Vector(5)
    v[1] = 23
    v[-1] = 45
    print(v)
    print(v[4])
    u = v + v
    print(u)
    total = 0

    for entry in v:
        total += entry
    
    print(total)


class Range:
    """A class that mimics the built-in range class"""

    def __init__(self, start, stop=None, step=1) -> None:
        """Initialize a Range instance.
        
        Semantics is similar to in-built range class.
        """
        
        if step == 0:
            raise ValueError("step cannot be 0")
        
        if stop is None:
            start, stop = 0, start

        self._length = max(0, (stop - start + step - 1 ) // step)

        self._start = start
        self._step = step
    
    def __len__(self):
        """Return number of entries in the range"""
        return self._length
    

    def __getitem__(self, k):
        """Return entry at index k (using standard interpretation if negative)"""
        if k < 0:
            k += len(self)
        
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        
        return self._start + k * self._step



def range_check():
    """Experiment with custom Range class"""
    c_range = Range(10, 20, 2)
    print(c_range[11])



class CreditCard:
    """A customer credit card"""

    def __init__(self, customer, bank, acnt, limit, initial_deposit=None) -> None:
        """Create a new card instance.
        
        The initial balance is zero.

        parameters
        ==========
        customer    name of customer ( e.g 'John Bowman')
        bank        name of bank ( e.g 'Kuda Bank')
        acnt        account identifier (e.g '5391 0375 9387 5309')
        limit       credit limit(measured in dollars)
        initial_deposit     amount to create the card with
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0 if not initial_deposit else initial_deposit

    def get_customer(self) -> str:
        """Returns customer name"""
        return self._customer

    def get_bank(self) -> str:
        """Returns bank name"""
        return self._bank
    
    def get_account(self) -> str:
        """Returns card identifying number"""
        return self._account
    
    def get_limit(self):
        """Return current credit limit"""
        return self._limit
    
    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient 
        limit.
        
        Return True if charge was processed; False if charge was
        denied.
        """
        if not isinstance(price, (int, float)):
            raise ValueError('A numeric instance is required')

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        """Process customer payment that reduces balance"""
        if not isinstance(amount, (int, float)):
            raise ValueError('A numeric instance is required')
        
        if amount < 0:
            raise ValueError("Cannot supply negative value")

        self._balance -= amount



class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr) -> None:
        """
        Create a new predatory credit card instance.

        The initial balance is Zero.

        customer    the name of the customer ( e.g 'John Doe' )
        bank        the name of the bank ( e.g 'Kuda Bank' )
        acnt        the account identifier ( e.g '3558 0365 9878 5309' )
        limit       credit limit (measured in dollars)
        apr         annual percentage rate (e.g 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit
        
        Return True if charge was processed.
        Return False and access $5 fee if charge is declined
        """
        success = super().charge(price)
        if not success:
            # penalty for accessing charge when credit limit is reached
            self._balance += 5
        return success
    
    def process_month(self):
        """Access monthly interest on outstanding balance"""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/2)
            self._balance *= monthly_factor
    


class Progression:
    """Iterator producing a generic progression.
    
    Default iterator produces the whole number 0,1,2,3 ...
    """

    def __init__(self, start=0) -> None:
        """Initialize current to the first value of the progression"""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.
        
        This should be overridden by a subclass to customize progression.

        By convention, if current is set to None, this designates the end
        of a finite progression.
        """
        self._current += 1
    
    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    
    def __iter__(self):
        """By convention an iterator must return itself as an iterator"""
        return self
    
    def print_progression(self, n):
        """Print next n values of the progression."""
        print(' '.join(str(next(self)) for j in range(n)))



class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression"""

    def __init__(self, increment=1, start=0) -> None:
        """Create a new arithmetic progression.
        
        parameters
        ==========
        increment   the fixed constant to add to each term (default 1)
        start       the first term of the progression (default=0)
        """
        super().__init__(start)
        self._increment = increment if increment else self._current

    def _advance(self):
        self._current += self._increment


class GeometricProgression(Progression):
    """Iterator producing an geometric progression"""

    def __init__(self, base=2, start=1) -> None:
        """Create a new geometric progression.

        parameters
        ==========
        base       the fixed constant multiplied to each term ( default 2 )
        start      the first term of progression ( default 1 ) 
        """
        super().__init__(start)
        self._base = base

    def _advance(self):
        """Update current value by multiplying it by the base value."""
        self._current *= self._base


class FibonacciProgression(Progression):
    """Iterator producing an fibonacci progression"""

    def __init__(self, first=0, second=1) -> None:
        super().__init__(first)
        self._next = second
    
    def _advance(self):
        self._current, self._next = self._next, self._current + self._next
        





def progression_check():
    # print("Progression Result")
    # p = Progression(30)
    # print(p.print_progression(30))

    # print("\n\nArithmetic Progression Result")
    # ap = ArithmeticProgression(30, 2)
    # print(ap.print_progression(30))

    # print("\n\nGeometric Progression Result")
    # gp = GeometricProgression(30, 2)
    # print(gp.print_progression(6))

    print("\n\nFibonacci Progression Result")
    fp = FibonacciProgression(4, 6)
    print(fp.print_progression(10))


if __name__ == "__main__":
    progression_check()
