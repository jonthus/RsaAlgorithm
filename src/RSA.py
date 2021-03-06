

"""
Moduuli, jolla generoidaan RSA:n avaimet ja suoritetaan enkryptio ja dekryptio.
"""

def generateKeys(p, q):
    """
    Funktio, joka generoi avaimet Primes-luokan ja RSA-algoritmin laskutoimituksilla.
    Args:
        p, q tai None, None
    Returns:
        e: public key
        d: private key
        n: toinen puoli avainta
    """
    e = 65537
    n = p * q
    phi = (p-1)*(q-1)
    d = pow(e, -1, phi)
    return e, d, n


def encryption(message, e, n):
    """
    Funktio, joka enkryptoi selkokielisen viestin.
    Args:
        message: selkokielinen viesti
        e: public key
        n: toinen puoli avainta
    Returns:
        res: enkryptoitu viesti
    """
    res = [pow(ord(c), e, n) for c in message]
    return res


def decryption(cipher, d, n):
    """
    Funktio, joka dekryptoi salatun viestin.
    Args:
        cipher: enkryptoitu viesti
        d: private key
        n: toinen puoli avainta
    Returns:
        res: selkokielinen viesti
    """
    res = [chr(pow(c, d, n)) for c in cipher]
    return ''.join(res)


# EOF
