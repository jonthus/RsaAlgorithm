import random

class Primes:
    """
    Luokka, jonka avulla generoidaan alkulukuja.

    Attributes:
        prime: Generoitu luku.
    """

    def PrimeGeneration(self, length=1024):
        """
        Generoidaan pariton alkuluvun kandidaatti (prime candidate).

        Args:
            length: alkuluvun pituus bitteinä

        Returns:
            Pariton alkuluku testattavaksi.
        """
        number = random.getrandbits(length)
        primes = []
        k = 1
        while k > 0:
            if Primes.Miller_Rabin(self, number, k):
                primes.append(number)
                k -= 1
                print(number)
            number += 1
        return number

    def Witness(self, a, n):
        """
        Witness-funktio Miller-Rabin testiä varten.
        Funktio palauttaa True, jos parametrin a avulla voidaan laskea, että n ei ole alkuluku.
        Jos palautetaan False, on n suurella todennäköisyydellä alkuluku.

        Args:
            a: satunnaisesti arvottu luku
            n: tutkittava mahdollinen alkuluku

        Returns:
            True: jos n ei ole varmasti alkuluku.
            False: jos suurella todennäköisyydellä alkuluku.
        """
        remainder = 1
        for y in range(n - 1):
            x = remainder
            remainder = (remainder * remainder) % n
            if remainder == 1 and x != 1 and x != n - 1:
                return True
            if y == 1:
                remainder = (remainder * a) % n
        if remainder != 1:
            return True
        return False

    def Miller_Rabin(self, n, k=6):
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
        if n < 2:
            return False
        for i in range(k):
            if Primes.Witness(self, random.randint(1, n - 1), n):
                return False
        return True

#TODO: Miller-Rabin -testaamisen nopeuttaminen.

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

if __name__ == "__main__":
    initiation = Primes()
    #prime = initiation.PrimeGeneration()
    prime = 2
    print(initiation.Miller_Rabin(prime, k=6))