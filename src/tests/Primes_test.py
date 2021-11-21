import random
import unittest
from .. import Primes

class TestPrimes(unittest.TestCase):

    def setUp(self):
        self.init = Primes.Primes()
        self.prime = self.init.PrimeGeneration()

    def test_Miller_Rabin(self):
        """
        Luokan Primes testaamista.
        Testaa Miller-Rabin testin toimintaa.

        Args:
            None

        Returns:
            assertEqual: onko testin tulos sama
        """
        prime = 5
        ans = self.init.Miller_Rabin(prime, k=6)
        self.assertEqual(ans, True)

    def test_Witness(self):
        return 0

    def test_PrimeGeneration(self):
        """
        Luokan Primes testaamista.
        Testaa ovatko generoidut alkuluvut saman pituisia.

        Args:
            none

        Returns:
            assertEqual: ovatko pituudet samat
        """

        test_length = 1024
        p = random.getrandbits(test_length)
        p |= (1 << test_length - 1) | 1
        prime_length = p.bit_length()
        self.assertEqual(prime_length, test_length)

    def test_CheckPrimality(self):
        test_value = False
        #ensimmäinen False
        prime = 1
        value = self.init.CheckPrimality(prime)
        self.assertEqual(value, test_value)

        test_value = True
        #viimeinen True
        prime = 17
        value = self.init.CheckPrimality(prime)
        self.assertEqual(value, test_value)

    #TODO: korjaa ylläoleva hitaampi primaalisuuden tarkistaminen
    #TODO: Miller-Rabinin toiminnan testaaminen.