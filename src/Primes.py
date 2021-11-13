import random
import unittest

class Primes():

    def PrimeGeneration(self, length=1024):
        """
        Generating a candidate prime number.

        :arg:
        length -- int -- length of the prime in bits

        :return:
        A possible prime number.
        """
        p = random.getrandbits(length)
        p |= (1 << length - 1) | 1

        return p

    def CheckPrime(self, n, k=128):
        """
        Checking if given number is a prime using
        the Miller-Rabin primality test.

        :arg:

        :return:
        False means n is not a prime.
        True means n is a prime.
        """
        if n!=int(n):
            return False
        n = int(n)
        s = 0
        d = n-1
        while d%2==0:
            d>>=1
            s+=1
        assert(2**s * d == n-1)

        for i in range(8):
            a = random.randrange(2, n)
            if Primes.trial_composite(a, d, n, s):
                return False
        return True

    def trial_composite(a, d, n, s):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True

if __name__ == "__main__":
    p = Primes()
    prime = p.PrimeGeneration()
    print(prime)
    print(p.CheckPrime(prime))
