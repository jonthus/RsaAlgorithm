import random

class Primes:
    """
    Luokka, jonka avulla generoidaan alkulukuja.

    Attributes:
        prime: Generoitu luku.
    """

    def __init__(self):
        self.prime = 0

    def PrimeGeneration(self, length=1024):
        """
        Generoidaan pariton alkuluvun kandidaatti (prime candidate).

        Args:
            length: alkuluvun pituus bitteinä

        Returns:
            Pariton alkuluku testattavaksi.
        """
        self.prime = random.getrandbits(length)
        self.prime |= (1 << length - 1) | 1
        return self.prime

    #def Miller_Rabin(self, n, k):
        """
        Tarkistetaan, onko annettu luku alkuluku käyttäen
        Miller-Rabin -testiä.

        Args:
            n: pariton luku, jonka primaalisuus testataan.
            k: parametri, joka vaikuttaa testin tarkkuuteen.

        Returns:
            True: luku on alkuluku suurella mahdollisuudella.
            False: luku ei varmasti ole alkuluku.
        """
        """
        Pseudocode:
        Input: n > 3, an odd integer to be tested for primality;
        Input: k, a parameter that determines the accuracy of the test
        Output: composite if n is composite, otherwise probably prime
        write n − 1 as 2s·d with d odd by factoring powers of 2 from n − 1
        LOOP: repeat k times:
           pick a randomly in the range [2, n − 2]
           x ← ad mod n
           if x  = 1 or x = n − 1 then do next LOOP
           for r = 1 .. s − 1
              x ← x2 mod n
              if x = 1 then return composite
              if x = n − 1 then do next LOOP
           return composite
        return probably prime
        """
#TODO: Miller-Rabin -testaamisen toteuttaminen.

    def CheckPrimality(self, prime):
        """
        Alkuluvun tarkistaminen hitaalla tavalla. Vertailukohta Miller-Rabin-testiä varten.

        Args:
            prime: Luku, joka tarkistetaan.

        Returns:
            True: jos luku on alkuluku.
            False: jos luku ei ole alkuluku.
        """
#TODO: Korjaa primaalisuuden testi sopivammaksi isoimmille luvuille. Alla oleva implementaatio on liian hidas.

        if prime <= 3:
            return prime > 1  # False
        if prime % 2 == 0 or prime % 3 == 0:
            return False
        i = 5
        while i ** 2 <= prime:
            if prime % i == 0 or prime % (i + 2) == 0:
                return False
            i += 6
        return True
