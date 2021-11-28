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

    def millerRabin(self, n, k=6):
        """
        Tarkistetaan, onko annettu luku alkuluku käyttäen
        Miller-Rabin -testiä.

        Args:
            p: potentiaalinen alkuluku, jonka primaalisuus testataan.
            k: testikierrosten määrä, joka vaikuttaa tarkkuuteen.

        Returns:
            True: luku on alkuluku suurella todennäköisyydellä.
            False: luku ei varmasti ole alkuluku.
        """

        d = n - 1
        t = 0

        while d % 2 == 0:  # jaetaan d tekijöihin jakamalla sitä kahdella
            d = d // 2
            t += 1

        for _ in range(k):
            a = random.randrange(2, n - 2)  # valitaan randomisoitu numero väliltä (2, n-2)
            x = pow(a, d, n)  # x = (a**d)%n
            if x != 1:
                i = 0
                while x != (n - 1):
                    if i == t - 1:
                        return False
                    else:
                        i = i + 1
                        x = pow(x, 2, n)  # x = (x**2)%n
        return True

    def checkPrimality(self, n):
        """
        Tarkistetaan ensin laskutoimituksen "n modulo alkuluku" avulla, jonka avulla voidaan
        poistaa suuri määrä epäalkulukuja ennen Miller-Rabinin suorittamista.

        Args:
            n: pariton luku, jonka primaalisuus testataan.

        Returns:
            True: luku on alkuluku suurella mahdollisuudella.
            False: luku ei varmasti ole alkuluku.
        """

        for prime in self.lowPrimeList:  # tarkistetaan, onko alkulukukandidaatin ja alkuvun jakojäännös 0
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
            n = random.getrandbits(1024)
            if Primes.checkPrimality(self, n):
                return n

if __name__ == "__main__":
    init = Primes()
    size = 1024
    n = init.primeGeneration(1024)
    print("Prime number: ", n)
    print("Primality check: ", init.checkPrimality(n))