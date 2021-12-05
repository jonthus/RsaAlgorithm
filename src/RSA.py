import Primes
import math
import random

def euclidean_gcd(e, phi):
    """
    Funktio, jonka avulla lasketaan Euclidean GCD.
    Args:

    Returns:

    """
    while phi:
        e, phi = phi, e % phi
    return e

def modular_inverse(e, phi):
    """
    Funktio, jonka avulla lasketaan Modular inverse.
    Args:

    Returns:

    """
    for i in range(1, phi):
        if e * i % phi == 1:
            return i
    return False

def calculate_rsa(p, q):
    """
    Funktio, jonka avulla lasketaan RSA enkryptiota varten tarvittavat termit.
    Args:

    Returns:

    """
    n = p*q
    phi = (p-1) * (q-1)
    while True:
        e = random.randrange(1, phi)
        gcd = euclidean_gcd(e, phi)
        d = modular_inverse(e, phi)
        if gcd == 1:
            break
    return e, d, n

def encryption(e, d, n):
    """
    Funktio, joka enkryptoi selkokielisen viestin.
    Args:

    Returns:

    """
    return 0

def decryption():
    """
    Funktio, joka dekryptoi selkokielisen viestin.
    Args:

    Returns:

    """
    return 0


if __name__ == "__main__":
    ans = calculate_rsa(5, 13)
    print(ans)
