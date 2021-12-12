import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Primes

class TestPrimes(unittest.TestCase):

    def setUp(self):
        self.init = Primes.Primes()
        self.prime = self.init.primeGeneration(1024)
        self.lowPrimesList = self.init.lowPrimes()

    def test_main(self):
        """
        Luokan main testaamista.
        Testaa luokan Primes ajamista.

        Args:
            None

        Returns:
            assertEqual: onko tulos sama
        """
        value = self.init.checkPrimality(self.prime)
        self.assertEqual(value, True)

    def test_lowPrimes(self):
        """
        Luokan lowPrimes testaamista.
        Testaa pienten alkulukujen generoimista.

        Args:
            None

        Returns:
            assertEqual: generoiko lista oikein
        """
        self.assertEqual(len(self.lowPrimesList), 168)

    def test_millerRabin(self):
        """
        Luokan Primes testaamista.
        Testaa Miller-Rabin testin toimintaa.

        Args:
            None

        Returns:
            assertEqual: onko testin tulos sama
        """
        prime = 5
        value = self.init.millerRabin(5, k=6)
        self.assertEqual(value, True)

    def test_checkPrimality(self):
        """
        Luokan checkPrimality testaamista.
        Testaa alkuluvut

        Args:
            None

        Returns:
            assertEqual: onko testin tulos sama
        """
        value = self.init.checkPrimality(self.prime)
        self.assertEqual(value, True)

    def test_primeGeneration(self):
        """
        Luokan primeGeneration testaamista.
        Testaa ovatko generoidut alkuluvut saman pituisia.

        Args:
            None

        Returns:
            assertEqual: ovatko pituudet samat
        """
        value = self.init.primeGeneration(1024)
        self.assertEqual(value.bit_length() > 1000, True)

# EOF
