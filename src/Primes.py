"""
Moduuli, jonka avulla generoidaan alkulukuja RSA:n laskemista varten.
"""

import random

class Primes:
    """
    Luokka, jonka avulla generoidaan suuria alkulukuja.
    """

    def __init__(self):
        self.lowPrimeList = Primes.lowPrimes(self)

    def lowPrimes(self):
        """
        Luo listan alkuluvuista väliltä 2 ja 1000.

        Args:
            None

        Returns:
            lowprimes: lista alkuluvuista väliltä 2 ja 1000.
        """
        lowprimes = []
        for i in range(2, 1000):
            if i > 1:
                for j in range (2, i):
                    if i % j == 0:
                        break
                else:
                    lowprimes.append(i)
        return lowprimes

    def millerRabin(self, n, k=40):
        """
        Tarkistetaan, onko annettu luku alkuluku käyttäen
        Miller-Rabin -testiä.

        Args:
            p: potentiaalinen alkuluku, jonka primaalisuus testataan.
            k: testikierrosten määrä, joka vaikuttaa testin tarkkuuteen.

        Returns:
            True: luku on alkuluku suurella todennäköisyydellä.
            False: luku ei varmasti ole alkuluku.
        """

        if n % 2 == 0:
            return False

        r = 0
        d = n - 1
        while d % 2 == 0:  # faktoroidaan pois kahden potenssit luvusta d
            r += 1
            d //= 2
        # n = 2^s * d, missä n on pariton luku

        for i in range(k):
            a = random.randrange(2, n - 1)  # generoidaan luku väliltä [2, n-2]
            x = pow(a, d, n)  # x = a^d % n
            if x == 1 or x == n - 1:
                continue
            for j in range(r):
                if x == n - 1:
                    break
                x = (x * x) % n  # x = x^x % n
            else:
                return False  # luku ei varmasti ole alkuluku
        return True  # luku on todennäköisesti alkuluku

    def checkPrimality(self, n):
        """
        Tarkistetaan annetun alkuluvun laskutoimituksen "n modulo alkuluku" avulla, jolla voidaan
        poistaa suuri määrä jaollisia lukuja ennen Miller-Rabinin suorittamista sen nopeuttamiseksi.

        Args:
            n: pariton luku, jonka primaalisuus testataan.

        Returns:
            True: luku on alkuluku suurella mahdollisuudella.
            False: luku ei varmasti ole alkuluku.
        """

        for prime in self.lowPrimeList:  # tarkistetaan, onko alkulukukandidaatin ja alkuluvun jakojäännös 0
            if n % prime == 0:
                return False

        return Primes.millerRabin(self, n)

    def primeGeneration(self, size):
        """
        Generoidaan luku ja tarkistetaan, onko se alkuluku.

        Args:
            size: haluttu alkuluvun koko bitteinä.

        Returns:
            n: Miller-Rabin testillä tarkistettu alkuluku
        """
        while True:
            n = random.getrandbits(size)
            if Primes.checkPrimality(self, n):
                return n


# EOF
